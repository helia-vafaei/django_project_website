from django.db import models

class book(models.Model):
    name = models.CharField(max_length=250 , blank=True , null=True)
    writer = models.CharField(max_length=250 , blank=True , null=True)
    summery = models.CharField(max_length=250 , blank=True , null=True)
    genre = models.CharField(max_length=250 , blank=True , null=True)
    