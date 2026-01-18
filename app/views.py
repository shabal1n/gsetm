from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def main_page(request):
    generators = GeneratorsRent.objects.all()
    clients = Client.objects.all()
    projects = Project.objects.all()

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
    # Загружаем категории И генераторы
    categories = GeneratorCategory.objects.all()
    generators_list = Generator.objects.all()

    return render(
        request,
        "generators.html",
        {
            "categories": categories,
            "generators": generators_list,
        },
    )


def generator_description(request, gen_id):
    try:
        generator = Generator.objects.get(id=gen_id)
        engine = Engine.objects.filter(generator=generator).first()
        alternator = Alternator.objects.filter(generator=generator).first()
        parameters = GeneratorParameters.objects.filter(generator=generator).first()
        images = GeneratorImage.objects.filter(generator=generator)

        context = {
            "generator": generator,
            "engine": engine,
            "alternator": alternator,
            "parameters": parameters,
            "images": images,
        }
        return render(request, "generator_description.html", context)
    except Generator.DoesNotExist:
        return HttpResponse("Generator not found", status=404)


def rent(request):
    rent_generators = GeneratorsRent.objects.all()
    return render(request, "rent.html", {"rent_generators": rent_generators})


def projects(request):
    projects_list = Project.objects.all()
    return render(request, "projects.html", {"projects": projects_list})


def contacts(request):
    return render(request, "contacts.html")


def generators_category(request, category_id):
    try:
        category = GeneratorCategory.objects.get(id=category_id)
        generators_list = Generator.objects.filter(category=category)
        categories = GeneratorCategory.objects.all()

        return render(
            request,
            "generators.html",
            {
                "generators": generators_list,
                "categories": categories,
                "current_category": category,
            },
        )
    except GeneratorCategory.DoesNotExist:
        return HttpResponse("Category not found", status=404)
