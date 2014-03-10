from django.contrib import admin

# Register your models here.
from company_app.models import Company, CompanyProject


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "github", "email", "user")
    search_fields = ("name",)
    readonly_fields = ("user",)


class CompanyProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "language", "company", "completed")
    search_fields = ("name",)
    readonly_fields = ("user",)

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyProject, CompanyProjectAdmin)


