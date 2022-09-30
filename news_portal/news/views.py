from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import *
from .filter import *


class PostList(ListView):
    # paginate_by = 3
    model = Post
    ordering = 'date_time'
    template_name = 'default.html'
    context_object_name = 'post'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'