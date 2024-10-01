from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'media']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control my-2'})
