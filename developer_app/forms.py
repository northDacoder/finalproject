from django.forms import ModelForm
from developer_app.models import Developer, Project

__author__ = 'northDacoder'
from django import forms
from django.forms.extras import SelectDateWidget



class DeveloperForm(ModelForm):
    class Meta:
        model = Developer


class ProjectForm(ModelForm):
    class Meta:
        model = Project



