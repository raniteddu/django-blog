from django.shortcuts import render
from blogs.models import Blog, Category

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True)
    non_featured_posts = Blog.objects.filter(is_featured=False, status='Published')
    context = {
        'featured_posts' : featured_posts,
        'non_featured_posts' : non_featured_posts
    }
    return render(request, 'home.html', context)