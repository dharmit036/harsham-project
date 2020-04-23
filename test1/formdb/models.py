# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class userdata(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    carnumber=models.CharField(max_length=10)
    carmodel=models.CharField(max_length=50)
    lastservice=models.CharField(max_length=10)
    serviceintime=models.CharField(max_length=10)
    predictedtime=models.CharField(max_length=10)
    def __unicode__(self):
       return str(self.firstname)
