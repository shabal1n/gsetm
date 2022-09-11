from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
                  path('', views.main_page, name='Главная'),
                  path('about', views.about_company, name='О компании'),
                  path('generators', views.generators, name='Генераторы'),
                  path('generators/<int:category_id>', views.generators_category, name='Генераторы'),
                  path('generator/<int:gen_id>', views.generator_description, name='Генератор'),
                  path('rent', views.rent, name='Аренда'),
                  path('projects', views.projects, name='Наши проекты'),
                  path('contacts', views.contacts, name='Контакты'),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
                       name='django.contrib.sitemaps.views.sitemap'),
                  path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
