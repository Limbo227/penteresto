from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    posts = Blog.objects.all()
    return render(request, 'gallery/index.html', {'posts':posts})

def post(request, id):
    post = Blog.objects.get(id=id)
    return render(request, 'gallery/post.html', {'post':post})