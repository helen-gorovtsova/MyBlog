from django.shortcuts import render

from posts.models import Post


def show_post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'show_post_list.html', context={'posts': posts})


def detail_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'detail_post.html', context={'post': post})