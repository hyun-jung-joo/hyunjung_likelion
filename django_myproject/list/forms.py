from django import forms
from .models import List

class PostModelForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['image', 'title', 'singer', 'content'] # 모든 필드 입력 받기