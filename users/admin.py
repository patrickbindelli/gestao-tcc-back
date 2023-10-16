from typing import Any
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.http.request import HttpRequest

from .models import UserAccount, Student, Teacher, Role


class StudentAdmin(admin.ModelAdmin):
    list_display = ["user", "course"]

    search_fields = [
        "user__first_name",
    ]

    # i should only be able to add new user and not select an existing one

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["user"].widget.can_add_related = True
        form.base_fields["user"].widget.can_change_related = False
        return form

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "user",
                    "course",
                ],
            },
        ),
    ]

    def get_readonly_fields(self, request: HttpRequest, obj: Student):
        readonly = []

        if obj:
            readonly.append("user")

        return readonly


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ["user"]
    search_fields = [
        "user__first_name",
    ]


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    extra = 0
    max_num = 1
    min_num = 1
    verbose_name = "Estudante"
    fk_name = "user"


class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    extra = 0
    max_num = 1
    min_num = 1
    verbose_name = "Professor"
    fk_name = "user"


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = UserAccount
        fields = ["email", "first_name", "last_name"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas não correspondem")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserAccount
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
        ]


class UserAccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["email", "first_name", "last_name", "is_staff", "is_superuser"]
    list_filter = ["is_superuser"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name"]}),
        ("Faculdade", {"fields": ["role"]}),
        ("Permissions", {"fields": ["is_staff", "is_superuser"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "first_name",
                    "last_name",
                    "email",
                    "role",
                    "password1",
                    "password2",
                ],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []
    inlines = []

    def get_inlines(self, request, obj=UserAccount):
        inlines = []

        if obj:
            if obj.role == Role.STUDENT:
                inlines.append(StudentInline)
            elif obj.role == Role.TEACHER:
                inlines.append(TeacherInline)

        return inlines


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(UserAccount, UserAccountAdmin)
admin.site.unregister(Group)
