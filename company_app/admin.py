from django.contrib import admin
from company_app.models import Company, CompanyProject, Language


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "github", "email", "user")
    search_fields = ("name",)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language",)

class CompanyProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "completed")
    search_fields = ("name",)

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyProject, CompanyProjectAdmin)
admin.site.register(Language, LanguageAdmin)

