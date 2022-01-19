from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import Category, News, Likes, Comments, Tags


# Register your models here.
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Tags)