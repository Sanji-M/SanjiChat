from django.core.paginator import Paginator
from .models import Category,Post
from django.shortcuts import render, get_object_or_404

def home(request):
    post_list = Post.objects.order_by('-created_at')
    paginator = Paginator(post_list, 5)  # Show 5 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, 'blog/home.html', {
        'page_obj': page_obj,
        'categories': categories
    })


    
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})

