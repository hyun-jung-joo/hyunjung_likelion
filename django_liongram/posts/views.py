from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from .models import Post 

def index(request):
    post_list = Post.objects.all().order_by('-created_at') # post의 전체 데이터 조회  / 최신꺼 맨 위로 -> orderby
    context = {
        'post_list' : post_list,
    }
    return render(request, 'index.html', context) # context 같이 보내주기 !!

def post_list_view(request) :
    post_list = Post.objects.all() # post의 전체 데이터 조회 
    # post_list = Post.objects.filter(writer=request.user) #filter : Post.writer가 현재 로그인인 것 조회
    context = {
        'post_list' : post_list,
    }
    return render(request, 'posts/post_list.html', context) # context 같이 보내주기 !!

def post_detail_view(request, id) :
    # 없으면 redirect -> 예외 처리
    try : 
        post = Post.objects.get(id=id) # 하나만 불러오기 -> get
    except Post.DoesNotExist :
        return redirect('index')
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)

@login_required # 로그인이 필요하다 
def post_create_view(request) :
    # request.method 확인하기 !! get -> 폼 화면 표시 / post -> index 화면으로 redirect
    if request.method == 'GET' :
        return render(request, 'posts/post_form.html')
    else :
        image = request.FILES.get('image') # post_form.html -> image, content 가져오기
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create( # model에 새로운 데이터 생성
            image=image,
            content=content,
            writer=request.user # 로그인(admin에서) 안한 상태이면 실행 안됨 -> admin에서 로그인 되어있을때는 실행되고 잘 뜬다 
        )
        return redirect('index')

@login_required # 작성자만 가능한 행위 - 로그인 필수 
def post_update_view(request, id) :
    #post = Post.objects.get(id=id) # 없는 id 로 들어갔을 때  아에 에러가 발생함
    post = get_object_or_404(Post, id=id, writer=request.user) 
    # writer=request.user 이어야 가능/ 아니면 404
    # 없는 id 로 들어갔을 때 에러 대신 404를 발생시킴 (윗 줄과 비교!!) -> 더 안전 ! 
    
    if request.method == 'GET' : # 수정하려고 수정하기에 접속했을 때 ! 
        context = { 'post': post }   
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST' : # new image 가져오기  -> 수정을 보냈을 때 ! 
        new_image = request.FILES.get('image') # post_form.html -> image, content 가져오기
        content = request.POST.get('content')
        print(new_image)
        print(content)
        
        # 새로운 이미지가 있을 때만, 변경 해주는 과정 !!  -> 같은 이미지가 계속 추가되는 것을 방지
        if new_image : 
            post.image.delete() # 새로운 이미지를 추가하기 전에 기존 이미지를 삭제
            post.image = new_image # 이미지 수정
        
        post.content = content # 내용 수정
        post.save() # 저장 
        return redirect('posts:post-detail', post.id) # 디테일 화면으로 리다이렉트 

# 작성자만 가능한 행위 - 로그인 필수
@login_required
def post_delete_view(request, id) :
    # user != writer -> return 404 -> 확인하는 것 
    post = get_object_or_404(Post, id=id, writer=request.user) # writer=request.user 이어야 가능/ 아니면 404
    
    # 윗줄 다른 방법 !
    # if request.user != post.writer : 
    #     raise Http404('잘못된 접근입니다.') 
    
    if request.method == 'GET' :
        context = {'post' : post}
        return render(request, 'posts/post_confirm_delete.html', context)
    else :
        post.delete() # 삭제 
        return redirect('index')








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