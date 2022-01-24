from django.contrib import admin
from django.contrib.admin import ModelAdmin
from apps.blog.models import Blog, BlogImage


class BlogImageAdmin(admin.TabularInline):
    model = BlogImage
    extra = 1


class BlogAdmin(ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    inlines = [BlogImageAdmin]


admin.site.register(Blog, BlogAdmin)

