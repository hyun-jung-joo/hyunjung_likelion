from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class List(models.Model) :
    image = models.ImageField(verbose_name='앨범 이미지', null=True, blank=True) 
    title = models.CharField(verbose_name="앨범 제목", max_length=128)
    singer = models.CharField(verbose_name='가수 이름', max_length=128)
    content = models.TextField(verbose_name="내용", default="")
    created_at = models.DateField(verbose_name="출시일", auto_now_add=True)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True) # 사용자와 연결
    
class Message(models.Model) :
    content = models.TextField(verbose_name='응원글 내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='List', on_delete=models.CASCADE) # fk 설정
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True) # 사용자와 연결