from django.shortcuts import render, redirect

# Create your views here.
from developer_app.forms import DeveloperForm
from developer_app.models import Developer


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