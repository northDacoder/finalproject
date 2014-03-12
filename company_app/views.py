from django.shortcuts import render, redirect
from company_app.forms import CompanyForm
from company_app.models import Company


def home(request):
    return render(request, "angular.html")

def companies(request):
    companies = Company.objects.all()
    data = {'companies': companies}
    return render(request, "companies/companies.html", data)


def new_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/companies")
    else:
        form = CompanyForm()
    data = {'form': form}
    return render(request, "companies/new_company.html", data)


def view_company(request, company_id):
    company = Company.objects.get(id=company_id)
    data = {"company": company}
    return render(request, "companies/view_company.html", data)


def edit_company(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            if form.save():
                return redirect("/company/{}".format(company_id))
    else:
        form = CompanyForm(instance=company)
    data = {"company": company, "form": form}
    return render(request, "companies/edit_company.html",data)


def delete_company(request, company_id):
    company = Company.objects.get(id=company_id)
    company.delete()
    return redirect("/companies")
