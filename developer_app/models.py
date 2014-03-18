from django.contrib.auth.models import User
from django.db import models
from company_app.models import CompanyProject, Language


class Developer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.URLField(max_length=1000)
    age = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)
    github = models.URLField(max_length=1000)
    languages = models.ManyToManyField(Language)
    description = models.CharField(max_length=6000)
    cover = models.ImageField(upload_to="images/developer_coverphoto")
    screenshot = models.ImageField(upload_to="images/developer_screenshots")
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class DeveloperProject(models.Model):
    project_name = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now=True)
    developer = models.ForeignKey(Developer, related_name="projects")
    company_project = models.ForeignKey(CompanyProject, related_name="developer_projects")
    project_screenshot = models.ImageField(upload_to="images/developer_screenshots")
    description = models.CharField(max_length=6000)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.name
