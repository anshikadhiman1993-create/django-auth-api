# core/urls.py
from django.contrib import admin
from django.urls import path, include
from core import views  # import your home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # this makes /api/register/ work
    path('', views.home),  # root URL
]
