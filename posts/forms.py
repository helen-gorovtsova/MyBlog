from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['published_date']
        widgets = {
            'post_body': forms.Textarea(attrs={'cols': 100, 'rows': 10, 'required': True}),
        }
