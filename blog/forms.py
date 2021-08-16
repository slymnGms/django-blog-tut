from django import forms
from django.db import models
from django.db.models import fields
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=('title','text',)