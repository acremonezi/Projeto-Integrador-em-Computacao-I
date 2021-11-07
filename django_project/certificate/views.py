from django.shortcuts import render, redirect
from django.http import HttpResponse

from certificate.models import Certificate

# Create your views here.

# Certificate
def certificate(request):
    # return HttpResponse('function certificate') # test view and urls 
    
    status = request.GET.get('status')
    return render(request, 'consulta.html', {'status': status})

# SignIN Validate
def search_certificate(request):
    # Form GET Info
    authentication_key = request.POST.get('authentication_key')
     
    # Auth Validation
    certificate_exist = Certificate.objects.filter(authentication_key = authentication_key)
    
    # Auth NOT Success
    if len(certificate_exist) == 0:
        return redirect('/certificate/?status=1')

    # Auth Success
    elif len(certificate_exist) > 0:
    
        return render(request, 'consulta.html', {'certificate_exist': certificate_exist})
          
        return redirect('/certificate/?status=2')
