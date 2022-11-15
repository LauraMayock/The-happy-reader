from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_review', views.add_review, name='add-review'),
    path('list_books', views.list_book, name='list-books'),
    path('update_review/<post_id>', views.update_review, name='update-review'),
    path('delete_review/<post_id>', views.delete_review, name='delete-review'),
    path("contact", views.contact, name="contact"),
    path('age0-2', views.age0_2, name="age0-2"),
    path('age3-5', views.age3_5, name="age3-5"),
    path('age6-8', views.age6_8, name="age6-8"),
    path('age9-11', views.age9_11, name="age9-11"),
    path('age-teen', views.ageteen, name="ageteen"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
    
]