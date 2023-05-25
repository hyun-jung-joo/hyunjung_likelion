from django.contrib import admin
from django.urls import path
from list import views
from .views import class_view

urlpatterns = [
    path('', views.listsHome, name='lists'),
    # path('create/', views.create, name='list-create'),
    path('create/', views.create_form, name='list-create'),
    path('<int:id>/', views.detail, name='list-detail'),
    # path('<int:id>/update/', views.update, name='list-update'),
    path('<int:id>/update/', views.update_form, name='list-update'),
    path('<int:id>/delete/', views.delete, name='list-delete'),
    # path('show/', class_view.as_view()),
    path('create_msg/<int:id>', views.create_msg, name='create_msg'),
    path('update_msg/<int:album_id>/<int:msg_id>', views.update_msg, name='update_msg'),
    path('delete_msg/<int:album_id>/<int:msg_id>', views.delete_msg, name='delete_msg'),
    
]