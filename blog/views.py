from django.shortcuts import render
from posts.models import Post

def homepage(request):
    latest_post = Post.objects.latest('date')
    post_count = Post.objects.all().count()
    return render(request, 'home.html', {
        'latest_post': latest_post,
        'post_count': post_count
    })

def about(request):
    return render(request, 'about.html')

def impress(request):
    return render(request, 'impress.html')

def privacy(request):
    return render(request, 'privacy.html')