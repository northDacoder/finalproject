from django.forms import ModelForm
from company_app.models import Company, CompanyProject


class CompanyForm(ModelForm):
    class Meta:
        model = Company


class CompanyProjectForm(ModelForm):
    class Meta:
        model = CompanyProject



