from django.forms import ModelForm
from developer_app.models import Developer, Project

class DeveloperForm(ModelForm):
    class Meta:
        model = Developer


class ProjectForm(ModelForm):
    class Meta:
        model = Project



