from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def main_page(request):
    generators = GeneratorsRent.objects.all()
    clients = Client.objects.all()
    projects = Project.objects.all()[:3]

    context = {
        "generators": generators,
        "clients": clients,
        "projects": projects,
    }
    return render(request, "main_page.html", context)


def about_company(request):
    about_data = AboutUsNumbers.objects.first()
    return render(request, "about_company.html", {"about": about_data})


def generators(request):
    generators_list = GeneratorsRent.objects.all()
    return render(request, "generators.html", {"generators": generators_list})


def generator_description(request, gen_id):
    generator = GeneratorsRent.objects.get(id=gen_id)
    return render(request, "generator_description.html", {"generator": generator})


def rent(request):
    return render(request, "rent.html")


def projects(request):
    projects_list = Project.objects.all()
    return render(request, "projects.html", {"projects": projects_list})


def contacts(request):
    return render(request, "contacts.html")


def generators_category(request, category_id):
    return render(request, "generators.html")


def get_price_KZT():
    return HttpResponse("Price in KZT")
