from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.main_page, name='Главная'),
                  path('about', views.about_company, name='О компании'),
                  path('generators', views.generators, name='Генераторы'),
                  path('generator/<int:gen_id>', views.generator_description, name='Генератор'),
                  path('rent', views.rent, name='Аренда'),
                  path('projects', views.projects, name='Наши проекты'),
                  path('contacts', views.contacts, name='Контакты'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
