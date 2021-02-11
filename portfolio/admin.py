from django.contrib import admin

from .models import ProjectCat, Project, ProjImag
# Register your models here.

class ProjImagAdmin(admin.StackedInline):
    model = ProjImag

@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjImagAdmin]
    class Meta:
        model = Project

@admin.register(ProjImag)
class ProjImagAdmin(admin.ModelAdmin):
    pass

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'categorie', 'show', 'project_date')
    list_display_links = ('id', 'name', 'categorie',)
    list_editable = ('show',)
    list_per_page = 20

# admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(ProjectCat)
# admin.site.register(Projects)