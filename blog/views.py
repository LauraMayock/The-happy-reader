from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, Contact, age_range
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BookReview, ContactForm
from django.contrib import messages



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status = 1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id = self.request.user.id).exists():
            liked = True
        saved = False
        if post.saves.filter(id = self.request.user.id).exists():
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
        return render(request, 
            'book_list.html', {'review': review})

    else:
        messages.success(request, ('You must log in.'))
        return redirect('home')
   


def add_review(request):
    submitted = False
    if request.method == "POST":
        form = BookReview(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_review?submitted = True')
    else:
        form = BookReview
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_review.html',
    {'form': form, 'submitted': submitted})


def delete_review(request, post_id):
    book = Post.objects.get(pk=post_id)
    if request.user == Post.author:
        Post.delete()
        messages.success(request, ("You have deleted this review."))
        return redirect('list-books')
    else:
        messages.success(request, ("You are not Authorized this review."))
        return redirect('list-books')


def contact(request):
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
    age = age_range.objects.get(id=1).age.all()
    return render(request, 'age0_2.html',
    {'age': age})


def age0_2(request):
    age2 = age_range.objects.get(id=2).age.all()
    return render(request, 'age0_2.html',
    {'age2': age2})
