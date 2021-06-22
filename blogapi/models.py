from django.db import models
from django.db.models.base import Model

class Blog(models.Model):
    title = models.CharField(max_length=100, null=True)
    blog = models.TextField()
    pic = models.ImageField(upload_to=None, height_field=None, width_field=None)
    bdate = models.DateTimeField(auto_now=True)