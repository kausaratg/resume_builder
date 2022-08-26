from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Portfolio(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    education = models.TextField(null=True, blank=True)
    certificate = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("index")
    

    def __str__(self):
        return self.first_name
