from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about', views.about_company, name='about_company'),
    path('generators', views.generators, name='generators'),
    path('generator/<int:gen_id>', views.generator_description, name='generator_description'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
