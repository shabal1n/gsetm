from django.shortcuts import render


def main_page(request):
    return render(request, 'main_page.html')


def about_company(request):
    return render(request, 'about_company.html')
