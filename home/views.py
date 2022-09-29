from django.shortcuts import render
from .models import Post


## Implementing CRUD


def list_view(request):
    if request.is_authenticated:
        post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'home/list_view.html', context)


def detail_view(request, pk):
    pass





