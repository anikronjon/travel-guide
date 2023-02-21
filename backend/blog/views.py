from django.shortcuts import render, get_object_or_404
from .models import Post


# post list view
def post_list_view(request):
    posts = Post.published.all()
    return render(request, 'blog/post/post_list.html', context={'posts': posts})


# post detail view
def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        created__year=year,
        created__month=month,
        created__day=day,
        slug=post,
    )
    return render(request, 'blog/post/post_detail.html', context={'post': post})
