from django.urls import path
from . import views

urlpatterns = [
    path('', views.certificate, name = 'certificate'),
    path('search_certificate/', views.search_certificate, name = 'search_certificate'),
]