from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('age', views.AgeBooks, name='age_books'),
    path('age', views.BooksByAge, name= 'age_list'),
    path('add_review', views.add_review, name='add-review'),
    
]