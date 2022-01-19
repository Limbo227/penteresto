from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
    all_news = News.objects.all()
    return render(request, 'gallery/index.html', {'all_news': all_news})

def post(request):
    return render(request, 'gallery/post.html')


