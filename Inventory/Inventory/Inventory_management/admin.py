# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
<<<<<<< HEAD
@admin.register(Desktop, Laptop, Mobile)
class ViewAdmin(admin.ModelAdmin):
	pass
=======
admin.site.register(Laptop),
admin.site.register(Desktop),
admin.site.register(Mobile)
>>>>>>> master
