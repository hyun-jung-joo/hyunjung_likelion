from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() # usermodel 

# 게시글 class
class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True) #verbose_name: 필드 이름 지정
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True) # 사용자와 연결
    
# 댓글 class    
class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일')
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE) # fk 설정
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True) # 사용자와 연결
    