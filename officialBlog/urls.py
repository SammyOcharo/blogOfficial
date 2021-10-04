from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverView, name='apioverview'),
    path('blog-list/', views.blogList, name='blog-list'),
    path('blog-detail/<str:pk>/', views.blogDetail, name='blog-detail'),
    path('blog-create/', views.createBlog, name='create-blog'),
    path('blog-update/<str:pk>/', views.updateBlog, name='blog-update'),
    path('blog-delete/<str:pk>/', views.deleteBlog, name='blog-delete'),
]