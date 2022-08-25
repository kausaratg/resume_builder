from django.db import models

# Create your models here.
class Portfolio(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    education = models.TextField(null=True, blank=True)
    certificate = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name
