from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Blog, Category,Comment
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
    if request.method =='POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {
        'single_blog' : single_blog,
        'comments' : comments,
        'comment_count' : comment_count
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