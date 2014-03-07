from django.db import models
from registration.models import User


class Developer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    github = models.URLField(max_length=1000)
    languages = models.TextField(max_length=1000)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Language(models.Model):
    language = models.CharField(max_length=50)

    def __unicode__(self):
        return self.language

class Project(models.Model):
    name = models.ForeignKey(Developer)
    language = models.ForeignKey(Language)
    company = models.CharField(max_length=1000)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.name
