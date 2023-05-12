from django.contrib import admin
from django.urls import path
from list import views
from .views import class_view

urlpatterns = [
    path('', views.listsHome, name='lists'),
    path('create/', views.create, name='create'),
    path('show/', class_view.as_view())
]