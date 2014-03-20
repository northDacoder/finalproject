from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, blank=True, null=True)
    description = models.TextField(max_length=6000)
    posted = models.DateTimeField(auto_now=True)
    website = models.URLField(max_length=1000, blank=True, null=True)
    github = models.URLField(max_length=1000)
    email = models.EmailField(null=False)
    cover = models.ImageField(upload_to="images/company_coverphoto")
    screenshot = models.ImageField(upload_to="images/company_screenshots")
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=50)

    def __unicode__(self):
        return self.language


class CompanyProject(models.Model):
    project_name = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company)
    language = models.ForeignKey(Language)
    completed = models.BooleanField()
    project_screenshot = models.ImageField(upload_to="images/developer_screenshots")
    description = models.TextField(max_length=6000)
    accepted_project = models.OneToOneField('developer_app.DeveloperProject', related_name="company_pick", blank=True, null=True)

    def __unicode__(self):
        return self.project_name
