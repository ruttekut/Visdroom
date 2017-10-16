# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blogpost(models.Model):
    '''Blog model'''
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateField(auto_now=False, auto_now_add=True)
    Images = models.ImageField(blank=True)
    author = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.title
