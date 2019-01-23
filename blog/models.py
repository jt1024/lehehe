from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    # ForeignKey(外键)对应多对一，外键要定义在“多”的一方
    # 本例通过author字段规定了文章与用户的关系，多篇文章可以对应一个用户，即文章对用户是"多对一"
    # related_name="blog_posts"的作用是，允许通过类User反向查询到BlogArticles，这个参数我们可以不设置，Django会默认以模型的小写作为反向关联名
    # 以后从User对象反向关联到他所写的BlogArticles，就可以使用user.blog_posts了
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)  # publish的倒序排序。此处是元祖，不要忘写后面的逗号

    def __str__(self):
        return self.title  # 对应后台文章列表中的默认显式字段
