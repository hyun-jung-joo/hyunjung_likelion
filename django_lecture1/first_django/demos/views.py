from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(request):
    # return HttpResponse('계산기 기능 구현 시작') # 템플릿을 사용하지 않고 응답을 할 수 있는 기능
    print(f'request = {request}')
    print(f'request = {type(request)}')
    # print(f'request.___dict__ = {request.__dict__}') # 데이터 직접 보기
    
    
    # 1. 데이터 확인 -> 값 확인 할 수 있는 방법 사용 ! 
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')
    
    # 2. 계산
    if operators == '+' :
        result = int(num1) + int(num2)
    elif operators == '-' :
        result = int(num1) - int(num2)
    elif operators == '*' :
        result = int(num1) * int(num2)
    elif operators == '/' :
        result = int(num1) / int(num2)
    else :
        result = 0

    # 3. 응답
    return render(request, 'calculator.html', {'result': result}) 