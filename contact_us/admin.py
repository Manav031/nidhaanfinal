from django.contrib import admin
from .models import ContactUs,Contact
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 5


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_email', 'contact_date')
    list_display_links = ('id', 'client_name')
    search_feilds = ('client_name', 'client_email')
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactUs, ContactUsAdmin)