from django import forms
from .models import Post, PostComment, Category

# Post Categories
cats = Category.objects.all().values_list('name', 'name')
# List of choices to select from
cats_list = []
for item in cats:
    cats_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'category', 'body', 'status')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Add a title'
                       }),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cats_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Add body content'
                                          }),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        
class EmailPostForm(forms.Form):
    """
    Share blog post form.
    """
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """
    Post comment form.
    """
    class Meta:
        model = PostComment
        fields = ('name', 'email', 'body')


class ContactForm(forms.Form):
    """
    Contact form.
    """
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

