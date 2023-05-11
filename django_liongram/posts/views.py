from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView

from .models import Post 

def index(request):
    return render(request, 'index.html')

def post_list_view(request) :
    return render(request, 'posts/post_list.html')

def post_detail_view(request, id) :
    return render(request, 'posts/post_detail.html')

def post_create_view(request) :
    return render(request, 'posts/post_form.html')

def post_update_view(request, id) :
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id) :
    return render(request, 'posts/post_confirm_delete.html')

def url_view(request):
    print('url_view()')
    data = {'code' : '001', 'msg' : 'OK'}
    return HttpResponse('<h1>url_view</h1>') # text -> html로 작동함
    # return JsonResponse(data) # dictionary 형태 반환 -> json 으로 반환
    
# url에 변수 정해놓은거 함수 매개변수로 넣어주기 - username
def url_parameter_view(request, username) :
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET : {request.GET}') # queryString 받기
    return HttpResponse(username)

#form 입력 
def function_view(request) :
    print(f'request.method: {request.method}')
    
    # get 일땐 get 만 출력 , post일 떈 post 만 출력
    if request.method == 'GET' :
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST' :
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

#ListView 상속 받기
class class_view(ListView) :
    model = Post # Post 기반 모델
    #ordering = ['-id'] # orderby랑 같은거
    template_name = 'cbv_view.html' # 출력 창
    
# class_view 클래스를 함수로 구현한다면!!   
def function_list_view(request) :
    object_list = Post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html', {'object_list' : object_list})