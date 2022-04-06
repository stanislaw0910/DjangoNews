from django import forms
from .models import Comments, News, Tags
from django.forms import ModelForm, TextInput


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['active']
        widgets={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of news'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News content'
            }),
            }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        exclude = ['news', 'user']
        widgets={
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Comment'
            }), }


class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'
        exclude = ['news',]
        widgets={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tag name',
            }), }
