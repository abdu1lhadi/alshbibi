from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-post_date', )

class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Company Name')
    email = models.EmailField(verbose_name='الايميل')
    nepersnt = models.CharField(max_length=50, verbose_name='الاسم', default= None)
    nopersnt = models.CharField(max_length=10, verbose_name='رقم الجوال', default= None)
    body = models.TextField(verbose_name='تعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    def __str__(self):
        return 'علق {} على {}.'.format(self.name, self.post)
    
    class Meta:
        ordering = ('-comment_date', )