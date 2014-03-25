from django.contrib import admin
from developer_app.models import Developer, DeveloperProject

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "email", "age", "posted", "github", "cover", "screenshot", "user")
    search_fields = ("name",)
    #readonly_fields = ("user",)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language",)

class DeveloperProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "created", "developer", "company_project", "project_screenshot", "completed")
    search_fields = ("name",)
    #readonly_fields = ("user",)

admin.site.register(Developer, DeveloperAdmin)
admin.site.register(DeveloperProject, DeveloperProjectAdmin)


