from django.shortcuts import render, redirect
from django.http import HttpResponse

from certificate.models import Certificate

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

# Certificate
def certificate(request):
    # return HttpResponse('function certificate') # test view and urls 
    
    status = request.GET.get('status')
    return render(request, 'search_certificate.html', {'status': status})

# Busca Certificado
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
    
        return render(request, 'search_certificate.html', {'certificate_exist': certificate_exist})
          
        return redirect('/certificate/?status=2')


# List Certificates
def my_certificates(request):
    # Home Acess Security
    if request.session.get('student'):
        student = request.session.get('student')
        certificate = Certificate.objects.filter(student = student)
        
        return render(request, 'my_certificates.html', {'certificate': certificate, 'student': student})
    else:
        return redirect('/auth/signin?status=2')
    
def print_certificate(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 700, "Certificado de Conclusao de Curso.")
    
    # Colocar os dados no certificadoS
 
        

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')