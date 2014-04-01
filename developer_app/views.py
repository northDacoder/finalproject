from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from developer_app.forms import SignupForm, LoginForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
    else:
        form = SignupForm()
    data = {"signup_form": form}
    return render(request, "signup.html", data)


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect("angular")
    else:
        form = LoginForm()
    data = {"login_form": form}
    return render(request, "login.html", data)



def angular(request):
    return render(request, "angular.html")
