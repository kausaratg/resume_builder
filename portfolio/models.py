from django.db import models
from django.urls import reverse
# from mysite.settings import PhoneNumberField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.
class Portfolio(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)  
    other_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField(verbose_name='Phone (+234..........)')
    links = models.TextField(blank=True)
    profile_image = models.ImageField(blank=True, upload_to="profile_img")
    about = models.TextField()
    education = models.TextField(null=True, blank=True)
    certificate_and_work_experience = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    Basic_information = models.TextField(blank=True, verbose_name="Biography (Age, Language, Location...)")

    def get_absolute_url(self):
        return reverse("cv_template")
    

    def __str__(self):
        return self.first_name
