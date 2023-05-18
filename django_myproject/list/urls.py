from django.contrib import admin
from django.urls import path
from list import views
from .views import class_view

urlpatterns = [
    path('', views.listsHome, name='lists'),
    path('create/', views.create, name='list-create'),
    path('<int:id>/', views.detail, name='list-detail'),
    path('<int:id>/update/', views.update, name='list-update'),
    path('<int:id>/delete', views.delete, name='list-delete'),
    path('show/', class_view.as_view())
]