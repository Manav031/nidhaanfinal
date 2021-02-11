from django.shortcuts import render,redirect
from .models import ContactUs,Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.
def contact_us(request):

    contact_us = ContactUs.objects.all()
    
    context = {
        'contact_us' : contact_us,

    }
    return render(request, 'contact_us/contact_us.html', context)

def contact(request):
    if request.method == 'POST':
        client_name = request.POST['client_name']
        client_email = request.POST['client_email']
        subject = request.POST ['subject']
        client_message = request.POST['client_message']

        contact = Contact(client_name=client_name, 
        client_email=client_email, subject=subject, client_message=client_message,)

        contact.save()

        # Send client_email
        send_mail(
            'Inquiry',
            'There has been Inquiry for   ' + client_name +'.  From Email: ' + client_email + '.  Subject: ' + subject + '. Message:' + client_message + '.  Sign into the admin panel for more',
            'nidhandesignstudio@gmail.com',
            ['nidhandesignstudio@gmail.com'],
            fail_silently=False
        )

        return redirect('contact_us')
