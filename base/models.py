from django.db import models

class Elements(models.Model):
    name = models.CharField(max_length=30,unique=True,blank=False,null=False)
    atomic_number = models.IntegerField(unique=True,blank=False,null=False)
    symbol = models.CharField(max_length=250,blank=False,null=False)
    discovery_year = models.CharField(max_length=5,blank=False,null=False,default='')
    group = models.IntegerField(blank=True,null=True)
    period = models.IntegerField(blank=True,null=True)
    atomic_weight = models.FloatField(blank=False,null=False)
    melting_point = models.IntegerField(blank=False,null=False)
    boiling_point = models.IntegerField(blank=False,null=False)
    electron_configuration = models.CharField(max_length=250,blank=False,null=False)
