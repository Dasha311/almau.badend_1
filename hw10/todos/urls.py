from django.urls import path
from . import views

urlpatterns = [
    path('blog/<int:user_id>/', UserBlogView.as_view(), name='user_blog'),
    path('posts/<int:post_id>/comments/', views.comment_list, name='comment_list'),
    path('posts/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/like/', views.like_post, name='like_post'),
    path('users/<int:user_id>/followers/', views.user_followers, name='user_followers'),
    path('users/<int:user_id>/follow/', views.follow_user, name='follow_user'),
]
