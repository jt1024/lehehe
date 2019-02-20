from django import template

register = template.Library()
from article.models import ArticlePost


@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()
