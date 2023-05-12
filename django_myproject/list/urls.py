from django.contrib import admin
from django.urls import path
from list import views

urlpatterns = [
    path('', views.listsHome, name='lists'),
    path('create/', views.create, name='create'),
]