from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from developer_app.models import Developer, Project

class DeveloperForm(ModelForm):
    class Meta:
        model = Developer


class ProjectForm(ModelForm):
    class Meta:
        model = Project



class UserForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "password": forms.PasswordInput
        }



class SignupForm(UserForm):
    confirm_password = forms.CharField(
        widget = forms.PasswordInput
    )

    def clean(self):
        password = self.cleaned_data.get("password")
        password_conf = self.cleaned_data.get("confirm_password")
        if password is not None and password != password_conf:
            raise forms.ValidationError(
                "Password confirmation does not match password"
            )

        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )
