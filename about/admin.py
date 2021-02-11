from django.contrib import admin

from .models import About,Service,Detail
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 20

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','service_title', 'show')
    list_display_links = ('id','service_title')
    list_editable = ('show',)
    list_per_page = 20

class DetailAdmin(admin.ModelAdmin):
    list_display = ('id','num')
    list_display_links = ('id','num')
    list_per_page = 20

admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Detail, DetailAdmin)