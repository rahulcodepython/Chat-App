from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatHomeView, name='index'),
]