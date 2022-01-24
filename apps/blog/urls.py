from django.urls import path
from apps.blog.views import (
    BlogListView,
    BlogGallery,
    blog_detail,

)

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('detail/<str:slug>/', blog_detail, name='blog_detail'),
    path('courses/', BlogGallery.as_view(), name='blog_gallery'),
]