from django import forms
from .models import Blog, Image
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        fields = ('title', 'content', 'status',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
