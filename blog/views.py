from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


def blog_list(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/blog_list.html", {"blogs": blogs})


def blog_detail(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "blog/blog_detail.html", {"article": article, "publish": pub})
