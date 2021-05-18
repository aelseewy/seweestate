from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    number = PhoneNumberField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/teams/', blank=True, null=True)
    company_name = models.CharField(max_length=255,blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    user_name = models.CharField(max_length=255,blank=True, null=True)
    facebook_link = models.URLField(max_length=130)
    twitter_link = models.URLField(max_length=130)
    linkedin_link = models.URLField(max_length=130)
    google_plus_link = models.URLField(max_length=130)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


