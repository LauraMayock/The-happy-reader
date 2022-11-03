from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, age_range, book_author
from django.http import HttpResponseRedirect
from .forms import BookReview


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



def List_Book(request):
    book_list = Post.objects.all()
    return render(request, 'book_list.html',
    {'book_list': book_list})


def Show_Book(request, book_id):
    books = Post,objects.get(pk=book_id)
    return render(request, 'detailed_list.html',
    {'book': book})



def Add_Review(request):
    submitted = False
    if request.method == "POST":
        form = BookReview(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_review?submitted=True')
    else:
        form = BookReview
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_review.html', 
    {'form': form, 'submitted':submitted})



class update_review(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "reviews.html"



