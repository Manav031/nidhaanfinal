from django.shortcuts import render, get_object_or_404
from contact_us.models import ContactUs
from .models import Portfolio, ProjectCat, Project, ProjImag

# Create your views here.
def portfolio(request):
    contact_us = ContactUs.objects.all()
    portfolio = Portfolio.objects.order_by('-project_date').filter(show=True)
    context = {
        'contact_us' : contact_us,
        'portfolio' : portfolio,
    }
    return render(request, 'portfolio/portfolio.html', context)

def project(request, categorie):
    project = Project.objects.filter(categorie=str(categorie))
    # pp = Project.objects.all()
    contact_us = ContactUs.objects.all()
    
    context = {
        'contact_us' : contact_us,
        'portfolio' : portfolio,
        'project' : project
    }
    return render(request, 'portfolio/project.html', context)

def projectmain(request, id):
    proj = Project.objects.filter(id=id)
    project = get_object_or_404(Project,id=id)
    projimag = ProjImag.objects.filter(Project=project)
    context = {
        'project' : proj,
        'projimag' : projimag
    }
    return render(request, 'portfolio/pproj.html', context)