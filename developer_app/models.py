from django.contrib.auth.models import User
from django.db import models
from company_app.models import CompanyProject, Language


class Developer(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(max_length=10, null=True, blank=False)
    posted = models.DateTimeField(auto_now=True)
    website = models.URLField(max_length=1000, blank=True, null=True)
    github = models.URLField(max_length=1000)
    languages = models.ManyToManyField(Language)
    description = models.TextField(max_length=6000)
    cover = models.ImageField(upload_to="developer_coverphoto")
    screenshot = models.ImageField(upload_to="/developer_screenshots")
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class DeveloperProject(models.Model):
    project_name = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now=True)
    developer = models.ForeignKey(Developer, related_name="projects")
    company_project = models.ForeignKey(CompanyProject, related_name="developer_projects")
    project_screenshot = models.ImageField(upload_to="images/developer_screenshots")
    description = models.TextField(max_length=6000)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.name
