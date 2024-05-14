from django.db import models

# Create your models here.
class SiteSettings(models.Model):
    banner= models.ImageField(upload_to='media/site/')
    caption= models.TextField(max_length=100)
    site_name= models.CharField(max_length=100)
    site_logo= models.ImageField(upload_to='media/images/')
    site_description= models.TextField()
    site_address= models.TextField()
    site_phone= models.CharField(max_length=15)
    site_email= models.EmailField()
    site_fb= models.URLField()
    site_twitter= models.URLField()
    site_instagram= models.URLField()
    site_youtube= models.URLField()
    site_github= models.URLField()
    site_created_at= models.DateTimeField(auto_now_add=True)
    site_updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.site_name