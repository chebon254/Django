# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Device(models.Model):

    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return format(self.type)

class Desktop(Device):
    pass

class Laptop(Device):
    pass

class Mobile(Device):
    pass
