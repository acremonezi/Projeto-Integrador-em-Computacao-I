from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def signup(request):
    return HttpResponse('funcao signup')

def signin(request):
    return HttpResponse('funcao signin')

