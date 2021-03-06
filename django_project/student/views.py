import hashlib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import Student

# Create your views here.

# SignUP
def signup(request):
    # return HttpResponse('function signup') // test view and urls 
    
    # Block logedIN users to access singUP again
    if request.session.get('student'):
        return redirect("/home")

    status = request.GET.get('status')
    return render(request, 'signup.html', {'status': status})


# SignIN
def signin(request):
    # return HttpResponse('function signin') // test view and urls

    # Block logedIN users to access singIN again
    if request.session.get('student'):
        return redirect("/home")

    status = request.GET.get('status')
    return render(request, 'signin.html', {'status': status})

# SignUP Validate
def signup_validate(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    # Check if e-Mail Exist:
    student_exist = Student.objects.filter(email=email)

    if len(student_exist) > 0:
        # e-Mail Exist:
        return redirect('/auth/signup?status=1')

    # Validate Empty Fields:
    if len(nome.strip()) == 0 or len(sobrenome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/signup?status=2')

    # Validade Password:
    if len(senha) < 8 or len(senha) > 12:
        # Password lengh is not Between 8 and 12 characters:
        return redirect('/auth/signup?status=3')
    
    try:
        # Create a DB instance:
        senha = hashlib.sha256(senha.encode()).hexdigest()
        student = Student(firstname=nome,
                        lastname=sobrenome,
                        email=email,
                        password=senha)

        # Save into the DB:
        student.save()
        return redirect('/auth/signup?status=0')

    except:
        return HttpResponse('Erro Interno do Sistema! Por favor, tente novamente mais tarde.')

# SignIN Validate
def signin_validate(request):
    # Form GET Info
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    # Auth Validation
    senha = hashlib.sha256(senha.encode()).hexdigest()
    student = Student.objects.filter(email = email).filter(password = senha)

    # Auth NOT Success
    if len(student) == 0:
        return redirect('/auth/signin?status=1')

    # Auth Success
    elif len(student) > 0:
        request.session['student'] = student[0].id

        return redirect('/home/')

def exit(request):
    request.session.flush()
    return redirect('/auth/signin')