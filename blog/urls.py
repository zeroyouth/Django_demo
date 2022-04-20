from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post-write/', views.blog_post_write),
    path('home/', views.blog_home),
    path('post-view/<int:post_id>', views.blog_post_view)
]