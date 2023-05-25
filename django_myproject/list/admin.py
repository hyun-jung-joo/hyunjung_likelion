from django.contrib import admin
from .models import List, Message

#new class 추가 -> 댓글 불러오는 것
class MessageInline(admin.TabularInline) :
    model = Message
    extra = 5 # 기본 개수
    min_num = 0 # 최소 개수
    max_num = 8 # 최대 개수
    verbose_name = '응원메시지' # 나오는 이름 
    verbose_name_plural = '응원메시지'

@admin.register(List)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'singer', 'content', 'created_at') # model의 속성 명들 집어넣기
    list_filter = ('singer',)
    search_fields = ('title', 'singer',)
    search_help_text = '제목 또는 가수 검색이 가능합니다.'
    inlines = [MessageInline] 
    actions = ['make_delete']
    
    def make_delete(modeladmin, request, queryset) :
            for item in queryset : # queryset이 선택한 post가 된다 
                item.image =''
                item.title='운영 규정 위반으로 인한 게시글 삭제 처리.' # 내용 수정
                item.singer=''
                item.content=''
                item.save() # 저장
                
                
admin.site.register(Message)