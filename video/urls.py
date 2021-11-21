from django.urls import path
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_video, name='upload_video'),
    path('dashboard/', views.dashboard, name="dashboard")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
