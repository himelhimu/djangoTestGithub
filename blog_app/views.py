from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
import logging
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
logger = logging.getLogger(__name__)


def index(request):
    posts = Post.objects.all()
    logger.error("Size of post")
    return render(request, 'blog_app/blog_post_list.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog_app/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_app/post_edit.html', {'form': form})
