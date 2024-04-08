from django.shortcuts import render,get_object_or_404
from .models import Blog, Category
from django.db.models import Q


def posts_by_category(request, category_id):
    catagory = get_object_or_404(Category, pk=category_id)
    posts = Blog.objects.filter(category=category_id)
    context = {
        'catagory': catagory,
        'posts' : posts
    }
    return render(request, 'posts_by_category.html', context)

def blog(request,slug):
    single_blog = get_object_or_404(Blog, slug=slug)
    context = {
        'single_blog' : single_blog
    }
    return render(request, 'blog.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword)|Q(short_description__icontains=keyword)|Q(blog_body__icontains=keyword))
    context = {
        'blogs': blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)