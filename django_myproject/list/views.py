from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostModelForm, MessageForm
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import List, Message

# Create your views here.
def listsHome(request):
    object_list = List.objects.all().order_by('-created_at')
    paginator = Paginator(object_list, 4) # 4개씩 paginator
    pagnum = request.GET.get('page') # page 번호 get
    object_list = paginator.get_page(pagnum) # albums에 해당 페이지 번호에 해당하는 앨범들 저장 (갱신)
    return render(request, 'lists.html', {'object_list' : object_list})

@login_required
def create(request) : 
    if request.method == 'POST' or request.method == 'FILES':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        singer = request.POST.get('singer')
        content = request.POST.get('content')
        List.objects.create (
            image=image,
            title=title,
            singer=singer,
            content=content,
            writer=request.user
        )
        return redirect('lists')
    else:
        return render(request, 'form_create.html')
    
def create_form(request) : 
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('lists')
    else:
        form = PostModelForm
        return render(request, 'form_create2.html', {'form' : form})
    

def detail(request, id) :
    try :
        album = List.objects.get(id=id)
        message_form = MessageForm()
        context = {
            'album' : album,
            'message_form' : message_form
        }
    except List.DoesNotExist :
        return redirect('lists')
    return render(request, 'list_detail.html', context)

@login_required
def update(request, id) :
    album = get_object_or_404(List, id=id, writer=request.user)
    
    if request.method == 'GET' :
        context = {'album' : album }
        return render(request, 'form_create.html', context)
    elif request.method == 'POST' :
        new_image = request.FILES.get('image')
        title = request.POST.get('title')
        singer = request.POST.get('singer')
        content = request.POST.get('content')
        
        if new_image :
            album.image.delete()
            album.image = new_image
        if title :
            album.title = title
        if singer :
            album.singer = singer 
        album.content = content
        album.save()
        return redirect('list-detail', album.id)

def update_form(request, id) : 
    album = get_object_or_404(List, id=id, writer=request.user)
    
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=album)
        if form.is_valid() :
            form.save()
            return redirect('lists')
    else :
        form = PostModelForm()
        context = {
            'form' : form,
            'id' : id
        }
        return render(request, 'form_create2.html', context)
    
@login_required
def delete(request, id) :
    album = get_object_or_404(List, id=id, writer=request.user)
    if request.method == 'GET' :
        context = {'album' : album}
        return render(request, 'delete_confirm.html', context)
    else :
        album.delete()
        return redirect('lists')

def create_msg(request, id) :
    filled_form = MessageForm(request.POST)

    if filled_form.is_valid():        
        finished_form = filled_form.save(commit=False)      
        finished_form.post = get_object_or_404(List, pk=id)        
        finished_form.save()   
    return redirect('list-detail', id)

def update_msg(request, album_id, msg_id) :
    msg = Message.objects.get(id=msg_id)
    msg_form = MessageForm(instance=msg) # msg에 들어가 있는 내용을 -> msg_form
    
    if request.method == 'POST' :
        update_form = MessageForm(request.POST, instance=msg) # post 요청이 오면 -> post와 함께 온 데이터를 update form 으로 저장
        if update_form.is_valid() :
            update_form.save()
            return redirect('list-detail', album_id)
    else : #GET
        return render(request, 'msg_update.html', {'msg_form' : msg_form})
        #GET 요청이라면 msg_update.html을 띄워주고, 그 템플릿에는 앞서 저장한 msg_form의 변수가 전달됩니다.

def delete_msg(request, album_id, msg_id) :
    msg = Message.objects.get(id=msg_id)
    msg.delete()
    
    return redirect('list-detail', album_id)


class class_view(ListView) :
    model = List # Post 기반 모델
    ordering = ['id'] # orderby랑 같은거
    template_name = 'show_list.html' # 출력 창
    
    