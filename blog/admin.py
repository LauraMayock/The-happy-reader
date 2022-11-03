from django.contrib import admin
from .models import Post, Comment, book_author, Genre, age_range
from django_summernote.admin import SummernoteModelAdmin


@admin. register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'genre', 'age_range', 'status', 'created_on')
    ordering = ('title',)
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approve=True)


admin.site.register(book_author)
admin.site.register(Genre)
admin.site.register(age_range)
