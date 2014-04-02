from django.contrib import admin
from company_app.models import Company, CompanyProject, Language


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "user", "city", "state", "website", "phone", "posted", "screenshot")
    search_fields = ("name",)
    readonly_fields = ("posted",)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language",)

class CompanyProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "created", "company", "language", "completed", "project_screenshot")
    search_fields = ("project_name",)
    readonly_fields = ("created",)

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyProject, CompanyProjectAdmin)
admin.site.register(Language, LanguageAdmin)

