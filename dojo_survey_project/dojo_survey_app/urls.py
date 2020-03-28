from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_form', views.process),
    path('result', views.result),
    path('clear_session', views.clear_session)
]