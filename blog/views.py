from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, age_range, book_author
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



def AgeBooks(request):
    age_list = age_range.objects.all()
    return render (request, 'age.html',
        {'age_list': age_list})


class BooksByAge(generic.DeleteView):
    model = age_range


##class AuthorListView(generic.ListView):
  ##  """Generic class-based list view for a list of authors."""
 ##   model = book_author
 ##   paginate_by = 10


##class AuthorDetailView(generic.DetailView):
  ##  """Generic class-based detail view for an author."""
  ##  model = book_author

def add_review(request):
    form = BookReview
    return render(request, 'add_review.html', 
    {'form': form})