from django.db import models
from django.db.models.signals import pre_save
from utils.slug_generator import unique_slug_generators


class Blog(models.Model):
    title = models.CharField(max_length=150)
    bio = models.TextField()
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'{self.title}'


class BlogImage(models.Model):
    image = models.ImageField(upload_to='image')
    blog = models.OneToOneField(
        Blog,
        on_delete=models.CASCADE,
        related_name='blog_image'
    )

    def __str__(self):
        return f'{self.blog.title}'


def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Blog)
