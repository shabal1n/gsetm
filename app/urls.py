from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", views.main_page, name="Главная"),
    path("about/", views.about_company, name="О компания"),
    path("generators/", views.generators, name="Генераторы"),
    path("generator/<int:gen_id>/", views.generator_description),
    path("rent/", views.rent, name="Аренда"),
    path("projects/", views.projects, name="Наши проекты"),
    path("contacts/", views.contacts, name="Контакты"),
    path("category/<int:category_id>/", views.generators_category),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
