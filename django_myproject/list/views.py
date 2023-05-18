from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostModelForm
from django.views.generic import ListView

from .models import List

# Create your views here.
def listsHome(request):
    object_list = List.objects.all().order_by('id')
    return render(request, 'lists.html', {'object_list':object_list})

@login_required
def create(request) : 
    if request.method == 'POST':
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

def detail(request, id) :
    try :
        album = List.objects.get(id=id)
    except List.DoesNotExist :
        return redirect('lists')
    return render(request, 'list_detail.html', {'album': album})

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
        album.title = title
        album.singer = singer 
        album.content = content
        album.save()
        return redirect('list-detail', album.id)
    
@login_required
def delete(request, id) :
    album = get_object_or_404(List, id=id, writer=request.user)
    if request.method == 'GET' :
        context = {'album' : album}
        return render(request, 'delete_confirm.html', context)
    else :
        album.delete()
        return redirect('lists')


class class_view(ListView) :
    model = List # Post 기반 모델
    ordering = ['id'] # orderby랑 같은거
    template_name = 'show_list.html' # 출력 창