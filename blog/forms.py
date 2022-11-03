from django import forms
from django.forms import ModelForm
from .models import Post


# Form for user to create a book review.
class BookReview(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'book_author', 'age_range', 'genre', 'excerpt', 'content')
        labels = {
            'title': 'Book Title:',
            'author': 'Review Author',
            'book_author': 'Book Author',
            'age_range': 'Age Group',
            'excerpt': 'Book Blurb',
            'content': 'Book Review',
        }
    
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'author': forms.TextInput(attrs={'class': 'form-control'}),
        'book_author': forms.TextInput(attrs={'class': 'form-control'}),
    }