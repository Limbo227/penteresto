from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.db.models import F


# Create your views here.
class Index(ListView):
    model = Blog
    context_object_name = 'posts'
    template_name = 'gallery/index.html'


class PostView(DetailView):
    model = Blog
    context_object_name = 'postview'
    template_name = 'gallery/post.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     self.object.views = F('views') + 1
    #     self.object.save()
    #     self.object.refresh_from_db()
    #     return context
