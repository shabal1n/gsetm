from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.main_page, name='main_page'),
                  path('about/', views.about_company, name='about'),
                  path('generators/', views.generators, name='generators'),
                  path('generators/category/<int:category_id>', views.generator_category, name='gen_category'),
                  path('generator/<int:gen_id>', views.generator_description, name='generator'),
                  path('rent/', views.rent, name='rent'),
                  path('projects/', views.projects, name='projects'),
                  path('contacts/', views.contacts, name='contacts'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
