from django.contrib import admin
from accounts.models import UserAccount
from .models import ThesisProject, Invite, FileVersion
from django import forms
from django.core.exceptions import ValidationError


class ThesisProjectForm(forms.ModelForm):
    class Meta:
        model = ThesisProject
        fields = "__all__"

    authors = forms.ModelMultipleChoiceField(
        queryset=UserAccount.objects.filter(role=UserAccount.STUDENT),
    )

    # advisor = forms.Widget(queryset=User.objects.filter(role=User.TEACHER))

    def clean(self):
        cleaned_data = super().clean()

        advisor = cleaned_data.get("advisor")
        committee = cleaned_data.get("committee")
        defense_date = cleaned_data.get("defense_date")
        type = cleaned_data.get("type")

        if advisor and advisor.role != UserAccount.TEACHER:
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


class InviteAdmin(admin.ModelAdmin):
    actions = [accept_invite_and_create_research]


admin.site.register(ThesisProject, ThesisProjectAdmin)
admin.site.register(Invite, InviteAdmin)
