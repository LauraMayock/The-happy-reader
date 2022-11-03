from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('list_books', views.List_Book, name='list-books'),
    path('show_book/<book_id>', views.Show_Book, name='book'),
    path('add_review', views.Add_Review, name='add-review'),

    
]