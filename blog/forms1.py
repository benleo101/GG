from django import forms

from .models import Post

class PostForm1(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','image')