from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('age', views.all_age, name="listAge"),
    path('age/<slug:slug:pk', views.GenderPost.as_view()),

]