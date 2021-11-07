from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/get_certificate/', views.get_certificate, name = 'get_certificate'),
]