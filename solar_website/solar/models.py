from django.db import models

# Create your models he
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class SocialMediaLinks(models.Model):
    facebook_link = models.CharField(null=True,blank=True,max_length=200)
    instagram_link = models.CharField(null=True, blank=True,max_length=200)
    whatsapp_link = models.CharField(null=True, blank=True, max_length=200)