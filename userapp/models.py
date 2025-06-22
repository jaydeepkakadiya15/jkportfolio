from django.db import models

# Create your models here.


class user_contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    message = models.TextField(max_length=1000)