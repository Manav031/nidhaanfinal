from django.shortcuts import render, get_object_or_404
from contact_us.models import ContactUs
from about.models import About, Service, Detail
from blog.models import Project, CurrentSite
from portfolio.models import Portfolio, ProjectCat

choices = None

# Create your views here.
def index(request):
    global choices
    about = About.objects.all()
    for i in about:
        print(i.about_you_title)

    service = Service.objects.filter(show=True)
    detail = Detail.objects.all()
    project = ProjectCat.objects.all()
    choices = ProjectCat.objects.values('categorie')
    
    currentSite = CurrentSite.objects.order_by('-current_project_date').filter(show=True)

    contact_us = ContactUs.objects.all()

    portfolio = Portfolio.objects.order_by('-project_date').filter(show=True)

    context = {
        "home_page" : "active",
        'contact_us' : contact_us,
        'about' : about,
        'service' : service,
        'detail': detail,
        'currentSite' : currentSite,
        'project' : project,
        'portfolio' : portfolio,
    }
    return render(request, 'pages/index.html', context)
