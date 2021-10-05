from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# SignUP
def signup(request):
    # return HttpResponse('funcao signup') // teste view e urls 
    status = request.GET.get('status')
    return render(request, 'signup.html', {'status': status})

# SignIN
def signin(request):
    # return HttpResponse('funcao signin') // teste view e urls 
    status = request.GET.get('status')
    return render(request, 'signin.html', {'status': status})

