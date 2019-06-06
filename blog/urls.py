from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns =[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coffee/', views.coffee, name='coffee'),
    path('course/', views.course, name='course'),
    path('europe/', views.europeClassc, name='europe'),
    path('external/', views.external, name='external'),
    path('interior/', views.interior, name='interior'),
    path('women/', views.specialWomen, name='women'),
    path('dyes/', views.dyes, name='dyes'),
    path('upgrading/', views.upgrading, name='upgrading'),
    path('allcars/', views.allcars, name='allcars'),
    
]