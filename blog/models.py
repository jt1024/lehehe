from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    # BlogArticles表中的author， 是User表的外键
    # 通过author字段规定了用户与文章的关系，一个用户对应多篇文章，即用户对文章是"一对多"
    # related_name="blog_posts"的作用是，允许通过类User反向查询到BlogArticles
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)  # publish的倒序排序。此处是元祖，不要忘写后面的逗号

    def __str__(self):
        return self.title  # 对应后台文章列表中的默认显式字段
