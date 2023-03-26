from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, PostComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "snippet", "status")
        widgets = {"body": SummernoteWidget()}


class EmailPostForm(forms.Form):
    """
    Share blog post form.
    """

    name = forms.CharField(required=True, max_length=30)
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    to = forms.EmailField(required=True, widget=forms.EmailInput())
    comments = forms.CharField(required=False, widget=forms.Textarea())


class CommentForm(forms.ModelForm):
    """
    Post comment form.
    """

    class Meta:
        model = PostComment
        fields = ("name", "email", "body")


class ContactForm(forms.Form):
    """
    Contact form.
    """

    from_email = forms.EmailField(max_length=50, required=True)
    subject = forms.CharField(max_length=50, required=True)
    message = forms.CharField(max_length=300, widget=forms.Textarea, required=True)
