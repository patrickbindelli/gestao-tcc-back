from django.contrib import admin
from .models import UsefulLink, UsefulFile


class UsefulLinktAdmin(admin.ModelAdmin):
    list_display = ("title",)


class UsefulFiletAdmin(admin.ModelAdmin):
    list_display = ("title", "file")


admin.site.register(UsefulLink, UsefulLinktAdmin)

admin.site.register(UsefulFile, UsefulFiletAdmin)
