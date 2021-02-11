from django.urls import path

from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<categorie>', views.project, name='project'),
    path('project/<id>', views.projectmain, name='projectmain'),
]
