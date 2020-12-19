from django import forms
from .models import Myblog, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Myblog
        fields = '__all__'

        widgets = {
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type':'hidden' }),
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'snippet' : forms.TextInput(attrs={'class': 'form-control'}),
            #'header_image' : forms.ImageField({'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Myblog
        fields = ('title', 'title_tag','body','snippet')
        
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'snippet' : forms.TextInput(attrs={'class': 'form-control'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }
