from django.contrib import admin
from users.models import Student, Teacher
from .models import ThesisProject, Invite, FileVersion
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin import widgets


# class FileVersionInlineForm(forms.ModelForm):
#     class Meta:
#         model = FileVersion
#         exclude = ["comments"]


# class FileVersionInline(admin.TabularInline):
#     model = FileVersion
#     extra = 1
#     form = FileVersionInlineForm


class ThesisProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "approved", "approved_at", "type")
    # inlines = [FileVersionInline]
    readonly_fields = ["approved_at"]
    search_fields = [
        "advisor",
        "author",
    ]
    autocomplete_fields = ["advisor", "author"]
    raw_id_fields = ("advisor",)


def accept_invite_and_create_research(modeladmin, request, queryset):
    for invite in queryset:
        if not invite.accepted:
            research_title = f"Pesquisa de {invite.advised.user}"

            research = ThesisProject.objects.create(
                invite=invite,
                title=research_title,
                type=invite.type,
                advisor=invite.advisor,
                author=invite.advised,
            )

            research.save()

            invite.accepted = True
            invite.save()


accept_invite_and_create_research.short_description = "Aceitar convite e criar pesquisa"


class InviteAdmin(admin.ModelAdmin):
    actions = [accept_invite_and_create_research]
    readonly_fields = ["limit_date", "accepted"]

    search_fields = [
        "advisor",
        "advised",
    ]
    autocomplete_fields = ["advised", "advisor"]


admin.site.register(ThesisProject, ThesisProjectAdmin)
admin.site.register(Invite, InviteAdmin)
