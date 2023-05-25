from django import forms
from .models import List, Message

class PostModelForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['image', 'title', 'singer', 'content', 'writer'] 
        
class MessageForm(forms.ModelForm):
    class Meta: 
        model = Message 
        fields = ['content']