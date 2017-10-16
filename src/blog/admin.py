# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Blogpost


# Register your models here.
class PostModelAdmin (admin.ModelAdmin):
    list_display = ['__str__', 'timestamp', 'author']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']

    class meta:
        model = Blogpost


admin.site.register(Blogpost, PostModelAdmin)
