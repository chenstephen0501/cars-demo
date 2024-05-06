from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='root'),
    path('about', views.about, name='about'),
]