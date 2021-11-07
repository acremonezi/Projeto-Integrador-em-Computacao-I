from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

# Certificate
def certificate(request):
    return HttpResponse('function certificate') # test view and urls 
    
    #status = request.GET.get('status')
    #return render(request, 'signup.html', {'status': status})


def create_authentication_key():
      return str(random.randint(1000000000, 9999999999))