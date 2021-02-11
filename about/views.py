from django.shortcuts import render
from .models import About,Service,Detail
from contact_us.models import ContactUs
# Create your views here.
def about(request):
    about = About.objects.all()
    service = Service.objects.filter(show=True)
    detail = Detail.objects.all()
    contact_us = ContactUs.objects.all()

    context = {
        'about' : about,
        'service' : service,
        'detail': detail,
        'contact_us' : contact_us,
    }

    return render(request, 'about/about.html', context)

