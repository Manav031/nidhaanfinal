from django.shortcuts import render, get_object_or_404
from contact_us.models import ContactUs
from .models import Project,CurrentSite
# Create your views here.
def index(request):
    contact_us = ContactUs.objects.all()
    project = Project.objects.order_by('-project_date').filter(show=True)
    currentSite = CurrentSite.objects.order_by('-current_project_date').filter(show=True)

    context = {
        'contact_us' : contact_us,
        'project' : project,
        'currentSite' : currentSite,
    }
    return render(request, 'blog/blogs.html', context)

def blog(request, blog_id):
    project = get_object_or_404(Project, pk=blog_id)


    contact_us = ContactUs.objects.all()
    context = {
        'contact_us' : contact_us,
        'project' : project,
    }
    return render(request, 'blog/blog.html', context)

def cs(request, cs_id):
    currentSite = get_object_or_404(CurrentSite, pk=cs_id)



    contact_us = ContactUs.objects.all()

    context = {
        'contact_us' : contact_us,
        'currentSite' : currentSite,
    }
    return render(request, 'blog/cs.html', context)


def search(request):
    currentSite = CurrentSite.objects.order_by('-current_project_date').filter(show=True)
    contact_us = ContactUs.objects.all()

    queryset_list = Project.objects.order_by('-project_date').filter(show=True)
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
                queryset_list = queryset_list.filter(categorie__icontains=keywords)
    
    context = {
        'project' : queryset_list,
        'values': request.GET,
        'currentSite' : currentSite,
        'contact_us' : contact_us,
    }

    return render(request, 'blog/blogs.html', context)