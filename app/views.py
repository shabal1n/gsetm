from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def main_page(request):
    generators_categories = GeneratorCategory.objects.all()
    clients = Client.objects.all()
    projects_list = Project.objects.all()[:3]
    return render(
        request,
        "main_page.html",
        {
            "generators_categories": generators_categories,
            "clients": clients,
            "projects_list": projects_list,
        },
    )


def about_company(request):
    return render(request, "about_company.html")


def generators(request):
    return render(request, "generators.html")


def generator_description(request, gen_id):
    return render(request, "generator_description.html")


def rent(request):
    return render(request, "rent.html")


def projects(request):
    return render(request, "projects.html")


def contacts(request):
    return render(request, "contacts.html")


def generators_category(request, category_id):
    return render(request, "generators.html")


def get_price_KZT():
    return HttpResponse("Price in KZT")
