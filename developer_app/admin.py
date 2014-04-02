from django.contrib import admin
from developer_app.models import Developer, DeveloperProject

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "user", "age", "city", "state", "website", "github", "phone", "posted", "screenshot")
    search_fields = ("name",)
    readonly_fields = ("posted",)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language",)

class DeveloperProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "created", "developer", "company_project", "project_screenshot", "completed")
    search_fields = ("name",)
    readonly_fields = ("created",)

admin.site.register(Developer, DeveloperAdmin)
admin.site.register(DeveloperProject, DeveloperProjectAdmin)


