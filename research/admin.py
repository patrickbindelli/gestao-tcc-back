from django.contrib import admin
from users.models import UserAccount, Role
from .models import ThesisProject, Invite, FileVersion
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin import widgets


class ThesisProjectForm(forms.ModelForm):
    class Meta:
        model = ThesisProject
        fields = "__all__"

    authors = forms.ModelMultipleChoiceField(
        queryset=UserAccount.objects.filter(role=Role.STUDENT),
    )

    # advisor = forms.Widget(queryset=UserAccount.objects.filter(role=Role.TEACHER))

    def clean(self):
        cleaned_data = super().clean()

        advisor = cleaned_data.get("advisor")
        committee = cleaned_data.get("committee")
        defense_date = cleaned_data.get("defense_date")
        type = cleaned_data.get("type")

        if advisor and advisor.role != Role.TEACHER:
            raise ValidationError(
                "O orientador deve ser um professor (com papel TEACHER)."
            )

        if committee or defense_date and type != ThesisProject.TCC2:
            raise ValidationError(
                "Para projetos com banca ou data de defesa, o tipo de pesquisa deve ser TCC2."
            )


class FileVersionInlineForm(forms.ModelForm):
    class Meta:
        model = FileVersion
        exclude = ["comments"]


class FileVersionInline(admin.TabularInline):
    model = FileVersion
    extra = 1
    form = FileVersionInlineForm


class ThesisProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "approved", "approved_at", "type")
    form = ThesisProjectForm
    inlines = [FileVersionInline]
    search_fields = [
        "advisor",
    ]
    autocomplete_fields = ["advisor"]

    raw_id_fields = ("advisor",)


def accept_invite_and_create_research(modeladmin, request, queryset):
    TIPOS_DE_PESQUISA_CLASSE = {
        "TCC1": ThesisProject.TCC1,
        "TCC2": ThesisProject.TCC2,
    }

    for invite in queryset:
        if not invite.accepted:
            invite.accepted = True
            invite.save()

            research_class = TIPOS_DE_PESQUISA_CLASSE.get(invite.type)

            research_title = f"Research ({invite.type}) for {invite.recipient.first_name} {invite.recipient.last_name}"

            research = research_class.objects.create(
                title=research_title,
            )

            research.authors.add(invite.recipient)

            research.save()


accept_invite_and_create_research.short_description = (
    "Accept invite and create research"
)


class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = "__all__"

    # sender = forms.ModelChoiceField(
    #     queryset=UserAccount.objects.exclude(role=Role.STUDENT),
    #     widget=widgets.ForeignKeyRawIdWidget(),
    # )

    # receiver = forms.ModelChoiceField(
    #     queryset=UserAccount.objects.filter(role=Role.STUDENT),
    # )


class InviteAdmin(admin.ModelAdmin):
    actions = [accept_invite_and_create_research]
    form = InviteForm

    # raw_id_fields = ["sender", "receiver"]


admin.site.register(ThesisProject, ThesisProjectAdmin)
admin.site.register(Invite, InviteAdmin)
