from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, Contact, age_range, Comment
from django.http import HttpResponseRedirect
from .forms import BookReview, ContactForm, CommentForm
from django.contrib import messages


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

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


def update_review(request, post_id):
    book = Post.objects.get(pk=post_id)
    form = BookReview(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list-books')

    return render(request, 'update_review.html', 
    {'update_books': book, 'form': form})


def list_book(request):
    if request.user.is_authenticated:
        user = request.user.id
        review = Post.objects.filter(author=user)
        return render(request, 'book_list.html', {'review': review})

    else:
        messages.success(request, ('You must log in.'))
        return redirect('home')
   

def add_review(request):
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
    {'form': form, 'submitted': submitted})


def delete_review(request, post_id):
    review = Post.objects.get(pk=post_id)
    review.delete()
    return redirect('list-books')
  

def contact(request):
    """
    Submits contact us form to the admin dashboars only 

    """
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact?submitted = True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contact.html',
    {'form': form, 'submitted': submitted})


def age0_2(request):
    """
    Creates a view listing all the books for ages 0-2

    """
    age = age_range.objects.get(id=1).age.all()
    return render(request, 'age.html',
     {
                'age': age,
                "comments": comments,
            },
        )



def age3_5(request):
    """
    Creates a view listing all the books for ages 3-5

    """
    age = age_range.objects.get(id=2).age.all()
    return render(request, 'age.html', {'age': age})


def age6_8(request):
    """
    Creates a view listing all the books for ages 6-8

    """
    age = age_range.objects.get(id=3).age.all()
    return render(request, 'age.html', {'age': age})


def age9_11(request):
    """
    Creates a view listing all the books for 9-11

    """
    age = age_range.objects.get(id=4).age.all()
    return render(request, 'age.html', {'age': age})


def ageteen(request):
    """
    Creates a view listing all the books for teens

    """
    age = age_range.objects.get(id=5).age.all()
    return render(request, 'age.html', {'age': age})


