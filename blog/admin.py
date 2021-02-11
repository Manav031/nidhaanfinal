from django.contrib import admin

from .models import Project,CurrentSite
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'categorie', 'show', 'project_date')
    list_display_links = ('id', 'name', 'categorie',)
    list_editable = ('show',)
    list_per_page = 20

class CurrentSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'current_site_name', 'show', 'current_project_date')
    list_display_links = ('id', 'current_site_name',)
    list_editable = ('show',)
    list_per_page = 20



admin.site.register(Project,ProjectAdmin)
admin.site.register(CurrentSite, CurrentSiteAdmin)