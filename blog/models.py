from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Genre(models.Model):
    genre_name = models.CharField(max_length=50)
    genre_image = CloudinaryField('image', default="placeholder")
    slug = models.SlugField(max_length=500, unique=True)

    def __str__(self):
        return self.genre_name


class age_range(models.Model):
    age_name = models.CharField(max_length=50)
    age_image = CloudinaryField('image', default="placeholder")
    slug = models.SlugField(max_length=500, unique=True)

    class Meta:
        db_table = "age_range"

    def __str__(self):
        return self.age_name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    book_author = models.CharField(max_length=200, null=True, blank=True)
    age_range = models.ForeignKey(
        'age_range', on_delete=models.SET_NULL, null=True, related_name="age")
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    saves = models.ManyToManyField(
        User, related_name='blogpost_saves', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_saves(self):
        return self.saves.count()

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=158)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
