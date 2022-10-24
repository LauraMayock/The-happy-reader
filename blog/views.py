from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, age_range, Genre


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        saved = False
        if post.saves.filter(id=self.request.user.id).exists():
            saved = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "saved": saved
            },
        )



def all_age(request):
    age = age_range.objects.all()
    return render(request, 'age.html',
    {'age': age})

class GenderPost(View):
    
    model = Genre
    template_name = "age.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_queryset'] = Topic.objects.all()
        return context