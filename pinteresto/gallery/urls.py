from django.urls import path
from .views import *
from django.conf.urls.static import static
from pinteresto import settings

urlpatterns = [
    path('', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

