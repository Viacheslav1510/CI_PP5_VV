from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post


def blog_home(request):
    """
    A function to open blog page,
    provide existent posts and make pagination
    """
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    template = 'blog/blog.html'
    context = {
        'page_obj': page_obj
    }
    return render(request, template, context)
