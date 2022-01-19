from django.urls import path
from .views import *
from django.conf.urls.static import static
from pinteresto import settings

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<str:slug>', PostView.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

