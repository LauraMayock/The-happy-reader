from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, CreateView, ListView
from .models import Post
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm, CommentForm, BookReview
from django.contrib import messages


class PostList(ListView):
    """
    Takes the Post Model and makes sure they are
    approved and displayes them on the home page
    """
    model = Post
    template_name = "index.html"
    queryset = Post.objects.filter(status=1).order_by('created_on')
    paginate_by = 6


class PostDetail(View):
    """
    Gets full book detail with approved reviews
    """
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
                "commented": True,
                "CommentForm": CommentForm,
                "liked": liked,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Shows full book detail with approved reviews
        Current user can submit a review form for approval
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("?")
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
    """
    Users can update book reviews that they have
    created using a form
    """
    book = Post.objects.get(pk=post_id)
    form = BookReview(request.POST or None, instance=book)
    if book.author != request.user:
        return redirect('This is not your review')
    if form.is_valid():
        form.save()
        return redirect('list-books')

    return render(request,
                  'update_review.html',
                  {'update_books': book, 'form': form})


def list_book(request):
    """
    Lists the reviews that the user
    has created in one place
    """
    if request.user.is_authenticated:
        user = request.user.id
        review = Post.objects.filter(author=user)
        return render(request, 'book_list.html', {'review': review})

    else:
        messages.success(request, ('You must log in.'))
        return redirect('home')


class AddPostView(LoginRequiredMixin, CreateView):
    """
    This view makes sure the user is logged in
    before they can access the template
    Calls the AddBookForm from forms.py to add
    a book to the database
    """
    template_name = 'add_review.html'
    form_class = BookReview

    def get_success_url(self):
        """
        sets the reverse url for the
        successful addition of the book
        to the database
        """
        return reverse('list-books')

    def form_valid(self, form):
        """_summary_
        validates the form and adds a success message
        to the template once abook is successfully added
        Sets the automatic slug for the object created
        from the user input on the title and book author
        fields
        """
        form.instance.author = self.request.user
        messages.success(
            self.request,
            'You have added a new book and it has been flagged for approval!')
        form.slug = slugify(form.instance.title)
        return super().form_valid(form)

    

def delete_review(request, post_id):
    """
    Users can delete book reviews
    """
    rev = Post.objects.get(pk=post_id)
    context = {'rev': rev}

    if request.method == 'POST':
        rev.delete()
        messages.success(request, ('You have deleted this review sucessfully.'))
        return redirect('list-books')

    return render(request, 'delete.html', context)


def contact(request):
    """
    Submits contact us form to the admin dashboard only
    to be approved.
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
    """
    Users can view books specific to a childs age
    """
    view = Post.objects.filter(age_range=1)
    return render(request, 'age.html', {'view': view})


def age2(request):
    """
    Filters book by a specific age_range using and id
    """
    view = Post.objects.filter(age_range=2)
    return render(request, 'age.html', {'view': view})


def age3(request):
    """
    Filters book by a specific age_range using and id
    """
    view = Post.objects.filter(age_range=3)
    return render(request, 'age.html', {'view': view})


def age4(request):
    """
    Filters book by a specific age_range using and id
    """
    view = Post.objects.filter(age_range=4)
    return render(request, 'age.html', {'view': view})


def age5(request):
    """
    Filters book by a specific age_range using and id
    """
    view = Post.objects.filter(age_range=5)
    return render(request, 'age.html', {'view': view})


class PostLike(View):
    """
    when a review is liked the slug is noted
    and the like is counted. Total likes displayed
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            