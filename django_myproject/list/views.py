from django.shortcuts import redirect, render
from .forms import PostModelForm

# Create your views here.
def listsHome(request):
	return render(request, 'lists.html')

def create(request) : 
    if request.method == 'POST':
        form = PostModelForm(request.POST) # 입력 내용을 DB에 저장
        if form.is_valid():  
            form.save() 
            return redirect('lists') 
    else:
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})