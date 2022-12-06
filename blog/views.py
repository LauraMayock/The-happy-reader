from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, age_range
from django.http import HttpResponseRedirect
from .forms import BookReview, ContactForm, CommentForm
from django.contrib import messages


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

    def get_age_data(self, *args, **kwargs):
        age_menu = age_range.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["age_menu"] = age_menu


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
                "commented": True,
                "CommentForm": CommentForm,
                "liked": liked, 
                "saved": saved,
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        saved = False
        if post.saves.filter(id=self.request.user.id).exists():
            saved = True

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
                "saved": saved, 
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


def age1(request):
    view = Post.objects.filter(age_range=1)
    return render(request, 'age.html', {'view': view})

def age2(request):
    view = Post.objects.filter(age_range=2)
    return render(request, 'age.html', {'view': view})  

def age3(request):
    view = Post.objects.filter(age_range=3)
    return render(request, 'age.html', {'view': view})

def age4(request):
    view = Post.objects.filter(age_range=4)
    return render(request, 'age.html', {'view': view})

def age5(request):
    view = Post.objects.filter(age_range=5)
    return render(request, 'age.html', {'view': view})



class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostSave(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.savess.filter(id=request.user.id).exists():
            post.saves.remove(request.user)
        else:
            post.saves.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))       


def saved(request):
    saves = Post.objects.filter(saves)
    return render(request, 'saved.html', {'saves': saves})
