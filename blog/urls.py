from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_review', views.AddPostView.as_view(), name='add-review'),
    path('list_books', views.list_book, name='list-books'),
    path('update_review/<post_id>', views.update_review, name='update-review'),
    path('delete_review/<post_id>', views.delete_review, name='delete-review'),
    path("contact", views.contact, name="contact"),
    path('age1', views.age1, name='age-book1'),
    path('age2', views.age2, name='age-book2'),
    path('age3', views.age3, name='age-book3'),
    path('age4', views.age4, name='age-book4'),
    path('age5', views.age5, name='age-book5'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'), 
]
