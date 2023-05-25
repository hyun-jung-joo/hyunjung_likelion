from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import Post

# class PostBaseForm(forms.Form) :
#     CATEGORY_CHOICES = [
#         ('1', '일반'),
#         ('2', '계정'),
#     ]
#     image = forms.ImageField(label='이미지') 
#     content = forms.CharField(label='내용', widget=forms.Textarea, required=True) # widget 지정 -> textarea 사용 
#     category = forms.ChoiceField(label='카테고리',choices=CATEGORY_CHOICES) # choice (category 생성)

# ModelForm 
class PostBaseForm(forms.ModelForm) :
    class Meta: 
        model = Post
        fields = '__all__'
        
from django.core.exceptions import ValidationError
class PostCreateForm(PostBaseForm) :
    class Meta(PostBaseForm.Meta) :
        fields = ['image' , 'content'] 
    
    # validation - custom ! 
    def clean_content(self) :
        data = self.cleaned_data['content']
        if "비속어" == data:
            raise ValidationError("비속어를 사용하실 수 없습니다.")
        return data
        
class PostUpdateForm(PostBaseForm) :
    class Meta(PostBaseForm.Meta) :
        fields = ['image' , 'content'] 
        
class PostDetailForm(PostBaseForm) :
    def __init__(self, *args, **kwargs):
        super(PostDetailForm, self).__init__(*args, **kwargs)
        for key in self.fields :
            self.fields[key].widget.attrs['disabled'] = True
        