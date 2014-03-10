from django.contrib import admin
from developer_app.models import Developer, Project

# Register your models here.
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "github", "languages", "user")
    search_fields = ("name",)
    readonly_fields = ("user",)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "language", "company", "completed")
    search_fields = ("name",)
    readonly_fields = ("user",)

admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Project, ProjectAdmin)


