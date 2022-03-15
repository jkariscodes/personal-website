from django import forms
from .models import Post, PostComment

# cats = Category.objects.all().values_list('name', 'name')
# cat_list = [cat for cat in cats]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'header_image', 'body', 'snippet', 'status')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Add a post title'
                       }),
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'hemp', 'type': 'hidden'
                       }),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Add body content...'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Add a snippet for the blog post...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class EmailPostForm(forms.Form):
    """
    Share blog post form.
    """
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))


class CommentForm(forms.ModelForm):
    """
    Post comment form.
    """
    class Meta:
        model = PostComment
        fields = ('name', 'email', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.Form):
    """
    Contact form.
    """
    from_email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Your E-mail address'}
    ))
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email subject'}
    ))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'E-mail body...'}
    ))


# class SearchForm(forms.Form):
#     """
#     Search form for blog posts.
#     """
#     query = forms.CharField()

