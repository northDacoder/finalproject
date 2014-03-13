from django.shortcuts import render, redirect

# Create your views here.
from developer_app.forms import DeveloperForm
from developer_app.models import Developer


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
        return redirect("login")

    else:
        form = SignupForm()
    data = {'form': form}
    return render(request, "signup.html", data)


@login_required
def special_page(request):
    data = {}
    return render(request, "charities/charities.html", data)

def login1(request):
    if request.method == "POST":
        form1 = LoginForm(request.POST)
        if form1.is_valid():
            user = authenticate(username=form1.cleaned_data['username'], password=form1.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("charity_home.html")

    else:
        form1 = LoginForm()
    data = {'form1': form1}
    return render(request, "login.html", data)

def angular(request):
    return render(request, "angular.html")

def home(request):
    return render(request, "home.html")

def developers(request):
    developers = Developer.objects.all()
    data = {'developers': developers}
    return render(request, "developers/developers.html", data)


def new_developer(request):
    if request.method == "POST":
        form = DeveloperForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/developers")
    else:
        form = DeveloperForm()
    data = {'form': form}
    return render(request, "developers/new_developer.html", data)


def view_developer(request, developer_id):
    developer = Developer.objects.get(id=developer_id)
    data = {"developer": developer}
    return render(request, "developers/view_developer.html", data)


def edit_developer(request, developer_id):
    developer = Developer.objects.get(id=developer_id)
    if request.method == "POST":
        form = DeveloperForm(request.POST, instance=developer)
        if form.is_valid():
            if form.save():
                return redirect("/developer/{}".format(developer_id))
    else:
        form = DeveloperForm(instance=developer)
    data = {"developer": developer, "form": form}
    return render(request, "developers/edit_developer.html",data)


def delete_developer(request, developer_id):
    developer = Developer.objects.get(id=developer_id)
    developer.delete()
    return redirect("/developers")