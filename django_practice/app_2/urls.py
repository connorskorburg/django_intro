from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact', views.contact),
    path('home', views.home),
    path('<str:name>', views.name)
]