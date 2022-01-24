from django.shortcuts import render
from django.views import generic
from apps.blog.models import Blog, BlogImage


class BlogListView(generic.ListView):
    queryset = Blog.objects.all()[:6]
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_detail.html', locals())


class BlogGallery(generic.ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
