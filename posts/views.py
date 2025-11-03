from django.shortcuts import render
from .models import Post, Category
from django.core.paginator import Paginator


# Create your views here.
def posts_list(request, category_name=None):
    
    category_name = request.GET.get("category", category_name)
    posts = Post.objects.all().order_by('-date')

    if category_name:
        posts = posts.filter(category__title__iexact=category_name)

    categories = Category.objects.all()
    
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, 'posts/posts_list.html', {
        'posts': posts,
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_name,
    })

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    related_posts = post.get_related_posts()
    return render(request, 'posts/post_page.html', {
        'post': post,
        'related_posts': related_posts
    })