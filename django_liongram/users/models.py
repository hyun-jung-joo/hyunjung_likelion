from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager

class UserManager(DjangoUserManager) : 
    # 정의할 것이 3가지 !!
    #1
    def _create_user(self, username, email, password, **extra_fields):
        if not email :
            raise ValueError('이메일은 필수 값입니다. ')
        user = self.model(username=username, email=email, **extra_fields) # 데이터 생성
        user.set_password(password) # pwd : 해싱처리를 위해 패스워드는 따로 set을 해준다 ! (암호화)
        user.save(using=self._db) # 유저 저장
        return user
        
    #2 
    def create_user(self, username, email=None, password=None, **extra_fields): # 일반 사용자 
        extra_fields.setdefault('is_staff', False) # 일반 사용자니까 스테프가 아님
        extra_fields.setdefault('is_superuser', False) # 슈퍼유저도 false
        return self._create_user(username, email, password, **extra_fields)
        
    #3 
    def create_superuser(self, username, email=None, password=None, **extra_fields):  # 슈퍼유저 
        extra_fields.setdefault('is_staff', True) # super user == manager
        extra_fields.setdefault('is_superuser', True) # 슈퍼유저도 True
        return self._create_user(username, email, password, **extra_fields)
    

# user field Custom 
class User(AbstractUser) :
    phone = models.CharField(verbose_name='전화번호', max_length=11)
    
    objects = UserManager() # manager 연결 
    
# user field Extension 
class UserInfo(models.Model) :
    phone_sub = models.CharField(verbose_name='보조 전화번호', max_length=11) # 확장 부분
    user = models.ForeignKey(to='User', on_delete=models.CASCADE) # FK  