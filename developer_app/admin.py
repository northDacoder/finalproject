from django.contrib import admin
from developer_app.models import Developer, DeveloperProject

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "github", "user")
    search_fields = ("name",)
    #readonly_fields = ("user",)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language",)

class DeveloperProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "company_project", "completed")
    search_fields = ("name",)
    #readonly_fields = ("user",)

admin.site.register(Developer, DeveloperAdmin)
admin.site.register(DeveloperProject, DeveloperProjectAdmin)


