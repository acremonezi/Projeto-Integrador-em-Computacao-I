from django.urls import path
from . import views

urlpatterns = [
    path('', views.certificate, name = 'certificate'),
    path('search_certificate/', views.search_certificate, name = 'search_certificate'),
    path('my_certificates/', views.my_certificates, name = 'my_certificates'),
    path('my_certificates/print_certificate/', views.print_certificate, name = 'print_certificate'),
]