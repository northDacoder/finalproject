from django.contrib.auth.models import User
from django.db import models
from company_app.models import Company


class Developer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    github = models.URLField(max_length=1000)
    languages = models.TextField(max_length=1000)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    developersproject = models.ForeignKey(Developer, related_name="developerRelated")
    company = models.ForeignKey(Company, related_name="company")
    name = models.CharField(max_length=100)
    completed = models.BooleanField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
