import math
import logging

import requests
from django.shortcuts import render
from .models import *

logger = logging.getLogger(__name__)

USD_KZT_FALLBACK_RATE = 500


def main_page(request):
    generators_categories = GeneratorCategory.objects.all()
    clients = Client.objects.all()
    projects_list = Project.objects.all()[:3]
    return render(
        request,
        "main_page.html",
        {
            "categories": generators_categories,
            "clients": clients,
            "projects": projects_list,
        },
    )


def about_company(request):
    generators_categories = GeneratorCategory.objects.all()
    clients = Client.objects.all()
    about_numbers = AboutUsNumbers.objects.first()
    return render(
        request,
        "about_company.html",
        {
            "categories": generators_categories,
            "clients": clients,
            "about_numbers": about_numbers,
        },
    )


def generators(request):
    generators_categories = GeneratorCategory.objects.all()
    alternators = Alternator.objects.all()
    dollar_course = get_price_KZT()
    return render(
        request,
        "generators.html",
        {
            "categories": generators_categories,
            "alternators": alternators,
            "course": dollar_course,
        },
    )


def generator_description(request, gen_id):
    generators_categories = GeneratorCategory.objects.all()
    generator = Generator.objects.get(id=gen_id)
    images = GeneratorImage.objects.filter(generator_id=gen_id)
    engine = Engine.objects.get(generator_id=gen_id)
    alternator = Alternator.objects.get(generator_id=gen_id)
    generator_parameters = GeneratorParameters.objects.get(generator_id=gen_id)
    dollar_course = get_price_KZT()
    return render(
        request,
        "generator_description.html",
        {
            "categories": generators_categories,
            "generator": generator,
            "images": images,
            "engine": engine,
            "alternator": alternator,
            "params": generator_parameters,
            "range": range(len(images)),
            "course": dollar_course,
        },
    )


def rent(request):
    generators_categories = GeneratorCategory.objects.all()
    rent_generators = GeneratorsRent.objects.all()
    return render(
        request,
        "rent.html",
        {"categories": generators_categories, "rent_generators": rent_generators},
    )


def projects(request):
    generators_categories = GeneratorCategory.objects.all()
    projects2 = Project.objects.all()
    return render(
        request,
        "projects.html",
        {"categories": generators_categories, "projects": projects2},
    )


def contacts(request):
    generators_categories = GeneratorCategory.objects.all()
    return render(request, "contacts.html", {"categories": generators_categories})


def get_price_KZT():
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "USD", "to": "KZT", "q": "1.0"}

    headers = {
        "X-RapidAPI-Key": "16d1315cf5msheaa92765cffe447p1f31b5jsnbdf27d45f845",
        "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com",
    }

    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=5)
        response.raise_for_status()
        exchange_rate = float(response.text.strip())
        return math.ceil(exchange_rate)
    except (requests.RequestException, ValueError) as exc:
        logger.warning(
            "USD/KZT exchange API failed, using fallback rate %s. Error: %s",
            USD_KZT_FALLBACK_RATE,
            exc,
        )
        return USD_KZT_FALLBACK_RATE


def generators_category(request, category_id):
    generators_categories = GeneratorCategory.objects.all()
    alternators = Alternator.objects.filter(generator__category_id=category_id)
    dollar_course = get_price_KZT()
    return render(
        request,
        "generators.html",
        {
            "categories": generators_categories,
            "alternators": alternators,
            "course": dollar_course,
        },
    )
