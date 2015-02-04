from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes',
        required=False,
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'docfile']
