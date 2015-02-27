from django import forms

from models import BlogArticle, Comment

class BlogArticleForm(forms.ModelForm):
    class Meta:
        model = BlogArticle
        exclude = ['author', 'slug']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']