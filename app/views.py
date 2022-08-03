from django.shortcuts import render
from .models import *


def main_page(request):
    generators_categories = GeneratorCategory.objects.all()
    clients = Client.objects.all()
    projects = Project.objects.all()
    return render(request, 'main_page.html',
                  {'categories': generators_categories, 'clients': clients, 'projects': projects})


def about_company(request):
    generators_categories = GeneratorCategory.objects.all()
    clients = Client.objects.all()
    return render(request, 'about_company.html', {'categories': generators_categories, 'clients': clients})


def generators(request):
    generators_categories = GeneratorCategory.objects.all()
    alternators = Alternator.objects.all()
    return render(request, 'generators.html', {'categories': generators_categories, 'alternators': alternators})


def generator_description(request, gen_id):
    generators_categories = GeneratorCategory.objects.all()
    generator = Generator.objects.get(id=gen_id)
    images = GeneratorImage.objects.filter(generator_id=gen_id)
    engine = Engine.objects.get(generator_id=gen_id)
    alternator = Alternator.objects.get(generator_id=gen_id)
    generator_parameters = GeneratorParameters.objects.get(generator_id=gen_id)
    return render(request, 'generator_description.html',
                  {'categories': generators_categories, 'generator': generator, 'images': images, 'engine': engine,
                   'alternator': alternator, 'params': generator_parameters, 'range': range(len(images))})
