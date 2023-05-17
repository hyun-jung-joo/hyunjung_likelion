from django.contrib import admin
from django.conf import settings # conf -> settings의 모든 값들을 가져올 수 있다.
from django.conf.urls.static import static
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
    
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # create한 이미지가 그냥 폴더 내부가 아닌 media 폴더 내에 넣기 위해서 media 폴더와 연결해준다(+=)