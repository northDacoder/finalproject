from django.contrib import admin
from company_app.models import Company, CompanyProject, Language


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "description", "email", "posted", "github", "email", "cover", "screenshot", "user")
    search_fields = ("name",)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language",)

class CompanyProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "created", "company", "language", "completed", "project_screenshot", "description")
    search_fields = ("project_name",)

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyProject, CompanyProjectAdmin)
admin.site.register(Language, LanguageAdmin)

