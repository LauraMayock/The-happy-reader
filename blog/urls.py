from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_review', views.add_review, name='add-review'),
    path('list_books', views.list_book, name='list-books'),
    path('update_review/<post_id>', views.update_review, name='update-review'),
    path('delete_review/<post_id>', views.delete_review, name='delete-review'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("contact", views.contact, name="contact"),
    
    
]