from django.db import models
from datetime import datetime


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    project_main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    categorie = models.CharField(max_length=200)
    details_main = models.TextField(blank=True)
    detail_2 = models.TextField(blank=True)
    product_design = models.TextField(blank=True)
    product_design_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    design_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    design_detail_1 = models.TextField(blank=True)
    design_detail_2 = models.TextField(blank=True)
    design_detail_3 = models.TextField(blank=True)
    design_detail_4 = models.TextField(blank=True)
    design_detail_5 = models.TextField(blank=True)
    

    final_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    final_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    final_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    final_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    final_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    final_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    final_photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    final_photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    final_photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    final_photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    design_detail_3 = models.TextField(blank=True)
    design_detail_4 = models.TextField(blank=True)

    show = models.BooleanField(default=True)
    project_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name

class CurrentSite(models.Model):
    current_site_name = models.CharField(max_length=200)
    current_main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    current_categorie = models.CharField(max_length=200, blank=True)
    current_details = models.TextField(blank=True)


    current_details_2 = models.TextField(blank=True)
    current_design_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    current_design_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    current_design_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    current_design_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    current_design_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    

    current_thoughts = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)




    show = models.BooleanField(default=True)
    current_project_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.current_site_name
