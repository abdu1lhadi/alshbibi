from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns =[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('test1/', TemplateView.as_view(template_name='blog/index.html'), name='test'),
]