from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


# Create your models here.


class admin_register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    pro_img = models.ImageField(upload_to='profile_images/', default='')


class profile_bio(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    about = models.TextField()
    dob = models.DateField()
    age = models.PositiveIntegerField()
    website = models.URLField(blank=True, null=True)
    degree = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    description = models.TextField()
    pro_pic = models.ImageField(upload_to='profile_pics/', default='')


class banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    banner_img = models.ImageField(upload_to='banner_images/', default='')


class skills(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_percentage = models.PositiveIntegerField()


class Education(models.Model):
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_year = models.IntegerField(
        validators=[MinValueValidator(1950), MaxValueValidator(2030)]
    )
    end_year = models.IntegerField(
        validators=[MinValueValidator(1950), MaxValueValidator(2020)]
    )
    description = models.TextField(blank=True, null=True)


class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_year = models.IntegerField(
        validators=[MinValueValidator(1950), MaxValueValidator(2030)]
    )
    end_year = models.IntegerField(
        validators=[MinValueValidator(1950), MaxValueValidator(2020)]
    )
    desc_1 = models.TextField()
    desc_2 = models.TextField()
    desc_3 = models.TextField()
    desc_4 = models.TextField()

class Portfolio(models.Model):
    project_name = models.CharField(max_length=100)
    project_link = models.URLField(blank=True, null=True)
    desc_1 = models.TextField(default="")
    desc_2 = models.TextField(default="")
    desc_3 = models.TextField(default="")
    desc_4 = models.TextField(default="")


class Services(models.Model):
    service_title = models.CharField(max_length=100)
    service_desc = models.TextField()
    service_icon = models.CharField(max_length=100, default="bi-palette")
  


  
    




   