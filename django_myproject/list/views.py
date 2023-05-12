from django.shortcuts import redirect, render
from .forms import PostModelForm
from django.views.generic import ListView

from .models import List

# Create your views here.
def listsHome(request):
    object_list = List.objects.all().order_by('id')
    return render(request, 'lists.html', {'object_list':object_list})

def create(request) : 
    print(f'request.method: {request.method}')
    if request.method == 'POST':
        form = PostModelForm(request.POST) # 입력 내용을 DB에 저장
        print(f'request.POST: {request.POST}')
        if form.is_valid():  
            form.save() 
            return redirect('lists') 
    else:
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})

class class_view(ListView) :
    model = List # Post 기반 모델
    ordering = ['id'] # orderby랑 같은거
    template_name = 'show_list.html' # 출력 창