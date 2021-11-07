from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from course.models import Course
from certificate.models import Certificate

# Create your views here.

def home(request):
    # Home Acess Security
    if request.session.get('student'):
        course = Course.objects.all()
        
        student = request.session.get('student')
        return render(request, 'home.html', {'course': course, 'student': student})
    else:
        return redirect('/auth/signin?status=2')


# Solicita um Certificado
def get_certificate(request):
    student = request.POST.get('student')
    course = request.POST.get('course')
    
    try:
        # Create a DB instance:
        certificate = Certificate(student=student, course=course)
        # Save into the DB:
        student.save()
        return redirect('/home/?status=0')

    except:
        return HttpResponse('Erro Interno do Sistema! Por favor, tente novamente mais tarde.')
