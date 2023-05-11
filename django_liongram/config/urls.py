from django.contrib import admin
from django.urls import path, include

from posts.views import url_view, url_parameter_view, function_view, class_view, function_list_view, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view), # int, str 둘다 사용 가능
    path('fbv/', function_view),
    path('fbv/list/', function_list_view),
    path('cbv/', class_view.as_view(), name='cbv'), #class -> .as_view()
    
    path('', index, name='index'),
    path('posts/', include('posts.urls')), # post의 url
]
