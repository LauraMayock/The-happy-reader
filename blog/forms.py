from django import forms
from django.forms import ModelForm
from .models import Post


# Form for user to create a book review.
class BookReview(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'book_author', 'age_range', 'genre', 'excerpt', 'content')
