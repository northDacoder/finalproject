from django.contrib.auth.models import User
from django.db import models
from company_app.models import CompanyProject, Language


class Developer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    github = models.URLField(max_length=1000)
    languages = models.ManyToManyField(Language)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class DeveloperProject(models.Model):
    developer = models.ForeignKey(Developer, related_name="projects")
    company_project = models.ForeignKey(CompanyProject, related_name="developer_projects")
    name = models.CharField(max_length=100)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.name
