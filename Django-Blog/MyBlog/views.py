
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    posts = Post.objects.order_by('-id')
    paginator = Paginator(posts, 6)

    page = request.GET.get('p')
    posts = paginator.get_page(page)

    return render(request, 'MyBlog/index.html', {
        'posts': posts
    })


def see_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'MyBlog/see_post.html', {
        'post': post
    })


def see_library(request):
    library_posts = Post.objects.filter(
        category='11'
    )

    return render(request, 'MyBlog/see_library.html', {
        'library_posts': library_posts
    })


def see_language(request):
    language_posts = Post.objects.filter(
        category='12'
    )

    return render(request, 'MyBlog/see_language.html', {
        'language_posts': language_posts
    })


def see_news(request):
    news_posts = Post.objects.filter(
        category='13'
    )

    return render(request, 'MyBlog/see_news.html', {
        'news_posts': news_posts
    })


def search(request):
    term = request.GET.get('term')

    posts = Post.objects.order_by('-id').filter(
        Q(title__icontains=term) | Q(short_description__icontains=term),
    )

    return render(request, 'MyBlog/search.html', {
        'posts': posts
    })


def reference(request):
    reference_posts = Post.objects.filter(
        category='14'
    )

    return render(request, 'MyBlog/see_reference.html', {
        'reference_posts': reference_posts
    })


def about(request):
    return render(request, 'MyBlog/about.html')


