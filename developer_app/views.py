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


@login_required
def special_page(request):
    data = {}
    return render(request, "developer/developers.html", data)

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect("secret")
    else:
        form = LoginForm()
    data = {"login_form": form}
    return render(request, "login.html", data)


def angular(request):
    return render(request, "angular.html")

def home(request):
    return render(request, "home.html")

# def developers(request):
#     developers = Developer.objects.all()
#     data = {'developers': developers}
#     return render(request, "developers/developers.html", data)
#
#
# def new_developer(request):
#     if request.method == "POST":
#         form = DeveloperForm(request.POST)
#         if form.is_valid():
#             if form.save():
#                 return redirect("/developers")
#     else:
#         form = DeveloperForm()
#     data = {'form': form}
#     return render(request, "developers/new_developer.html", data)
#
#
# def view_developer(request, developer_id):
#     developer = Developer.objects.get(id=developer_id)
#     data = {"developer": developer}
#     return render(request, "developers/view_developer.html", data)
#
#
# def edit_developer(request, developer_id):
#     developer = Developer.objects.get(id=developer_id)
#     if request.method == "POST":
#         form = DeveloperForm(request.POST, instance=developer)
#         if form.is_valid():
#             if form.save():
#                 return redirect("/developer/{}".format(developer_id))
#     else:
#         form = DeveloperForm(instance=developer)
#     data = {"developer": developer, "form": form}
#     return render(request, "developers/edit_developer.html",data)
#
#
# def delete_developer(request, developer_id):
#     developer = Developer.objects.get(id=developer_id)
#     developer.delete()
#     return redirect("/developers")