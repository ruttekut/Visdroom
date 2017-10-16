# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blogpost


# Create your views here.
# class BlogpostListview(Listview):
class BlogListView(ListView):

    queryset = Blogpost.objects.all()


class BlogDetailView(DetailView):
    """docstring for BlogDetailView."""
    queryset = Blogpost.objects.all()
