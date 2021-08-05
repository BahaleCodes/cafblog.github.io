from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, EmailField, IntegerField

class Blog(models.Model):
    title = models.CharField(max_length=100, null=True)
    blog = models.TextField()
    pic = models.ImageField(upload_to=None, height_field=None, width_field=None)
    bdate = models.DateTimeField(auto_now=True)

class Sponsor(models.Model):
    sponsor_type = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=20)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=50)