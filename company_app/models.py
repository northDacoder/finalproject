from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    description = models.TextField(max_length=6000, blank=True, null=True)
    posted = models.DateTimeField(auto_now=True)
    website = models.URLField(max_length=1000, blank=True, null=True)
    github = models.URLField(max_length=1000, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cover = models.ImageField(upload_to="images/company_coverphoto", blank=True, null=True)
    screenshot = models.ImageField(upload_to="images/company_screenshots", blank=True, null=True)
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
    company = models.ForeignKey(Company, related_name='company_projects')
    language = models.ForeignKey(Language, blank=True, null=True)
    completed = models.BooleanField()
    project_screenshot = models.ImageField(upload_to="images/developer_screenshots", blank=True, null=True)
    description = models.TextField(max_length=6000, blank=True, null=True)
    accepted_project = models.OneToOneField('developer_app.DeveloperProject', related_name="company_pick", blank=True, null=True)

    def __unicode__(self):
        return self.project_name
