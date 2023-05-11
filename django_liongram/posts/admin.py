from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline) :
    model = Comment
    extra = 5 # 기본 개수
    min_num = 3 # 최소 개수
    max_num = 5 # 최대 개수
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content', 'created_at', 'view_count', 'writer') # model의 속성 명들 집어넣기
    # list_editable = ('content', )
    list_filter = ('created_at',) #tuple 이므로 하나일때 , 넣어주기 -> 리스트로 변환도 가능 
    search_fields = ('id', 'writer__username') # look up 기능 사용
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    readonly_fields = ('created_at', ) #readonly : 읽기 전용으로 출력해줌
    inlines = [CommentInline]
    actions = ['make_published']
    
    def make_published(modeladmin, request, queryset) :
        for item in queryset :
            item.content='운영 규정 위반으로 인한 게시글 삭제 처리.'
            item.save()

# admin.site.register(Comment) # 댓글을 뺴주기
