from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Course

# Create your views here.

def home(request):
    # Home Acess Security
    if request.session.get('student'):
        course = Course.objects.all()
        
        student = request.session.get('student')
        return render(request, 'home.html', {'course': course, 'student': student})
    else:
        return redirect('/auth/signin?status=2')
