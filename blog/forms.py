from django import forms
from django.forms import ModelForm
from .models import Post, Contact, Comment


# Form for user to create a book review.
class BookReview(forms.ModelForm):
    """
    Creates a form based on the Post model
    """
    class Meta:
        model = Post
        fields = (
            'title', 'book_author',
            'age_range',
            'genre', 'excerpt',
            'content')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'book_author': forms.TextInput(attrs={'class': 'form-control'}),
        'age_range': forms.Select(attrs={'class': 'form-control'}),
        'genre': forms.Select(attrs={'class': 'form-control'}),
        'excerpt': forms.TextInput(attrs={'placeholder': 'blog'}),
        'content': forms.TextInput(attrs={'class': 'form-control'}),
    }


class ContactForm(ModelForm):
    """
    Contact form
    """
    class Meta:
        model = Contact
        fields = '__all__'


class CommentForm(forms.ModelForm):
    """
    Comment form
    """
    class Meta:
        model = Comment
        fields = ('body',)
