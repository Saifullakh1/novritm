from django import forms
from apps.blog.models import Blog, BlogImage


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'bio']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'})
        }


class BlogImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-comtrol'})
        }