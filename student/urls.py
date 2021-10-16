from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),

    path('signup_validate/', views.signup_validate, name = 'signup_validate'),
    path('signin_validade/', views.signin_validate, name = 'signin_validate'),
]