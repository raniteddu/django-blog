from django.shortcuts import render,get_object_or_404
from .models import Blog, Category


def posts_by_category(request, category_id):
    catagory = get_object_or_404(Category, pk=category_id)
    posts = Blog.objects.filter(category=category_id)
    context = {
        'catagory': catagory,
        'posts' : posts
    }
    return render(request, 'posts_by_category.html', context)