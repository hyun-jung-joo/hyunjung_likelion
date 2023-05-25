from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # django 에서 지원하는 회원가입 폼

from .forms import UserCreateForm, SignUpForm

from users.models import User

def signup_view(request) :
    # GET 요청 시 HTML 응답
    if request.method == 'GET' :
        # form = UserCreateForm # 내가 만든 폼 
        # form = UserCreationForm # 잔고의 내장 회원가입 폼 이용
        form = SignUpForm # custom form
        context = {'form' : form}
        return render(request, 'accounts/signup.html', context)
    # POST 요청 시 데이터 확인 후 회원 생성
    else: 
        form = SignUpForm(request.POST)
        
        if form.is_valid() :
            # 회원가입 처리
            instance = form.save()
            return redirect('index')
        else :
            # redirect
            return redirect('accounts:signup')
    
# login 
def login_view(request) :
    # GET, POST 분리
    if request.method == 'GET' :
        # 로그인 HTML 응답
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm()})
    else :
        # 데이터 유효성 검사
        form = AuthenticationForm(request, data=request.POST) # 새로운 장고 폼을 사용한다 
        if form.is_valid() :
            # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache) 
            # 응답 
            return redirect('index')
        else :
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답 
            return render(request, 'accounts/login.html', {'form' : form})

    
    # 이렇게도 가능하다는 것 ! (하단 코드) - 폼말고 다른 방식의 방법 -> 위에서는 폼 방식을 쓸 거임
    # username = request.POST.get('username')
    # # 공백 허용 x 
    # if username == '' or username == None :
    #     pass
    # # id 가 없는 경우 
    # user = User.objects.get(username=username)
    # if user == None :
    #     pass
    # password = request.POST.get('password')
    
    
def logout_view(request) : 
    # 데이터 유효성 검사
    if request.user.is_authenticated : # 로그인 상태 라면 ! -> 함수명 사용
        # 비즈니스 로직 처리 - 로그아웃
        logout(request) # 로그아웃 제공함(장고에서)
    # 응답
    return redirect('index')