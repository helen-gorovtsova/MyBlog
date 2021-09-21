from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm
from .models import Post


def show_post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'show_post_list.html', context={'posts': posts})


def detail_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'detail_post.html', context={'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        print(form.errors)
    else:
        form = PostForm()
    return render(request, 'create_post.html', context={'form': form})
