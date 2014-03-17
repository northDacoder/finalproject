from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    github = models.URLField(max_length=1000)
    email = models.EmailField(null=False)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=50)

    def __unicode__(self):
        return self.language


class CompanyProject(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.name
