from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category

# Create your views here.


def home(request):
    return render(request, 'home.html')

def technology(request):
    return renderBlogCategory(request, "Technology")
    #return render(request, 'technology.html')

def travel(request):
    return renderBlogCategory(request, "Travel")
    #return render(request, 'travel.html')

def food(request):
    return renderBlogCategory(request, "Food")
    #return render(request, 'food.html')

def fashion(request):
    return renderBlogCategory(request, "Fashion")
    #return render(request, 'fashion.html')

def renderBlogCategory(request, categoryName):
    categoryToFilter = get_object_or_404(Category, name=categoryName)
    posts = Post.objects.filter(category=categoryToFilter).order_by('-created_at')
    context = {'category': categoryName, 'posts': posts}
    return render(request, 'blog_category_post_list.html', context)    

def blogposttemplate(request):
    return render(request, 'blogposttemplate.html')

def blogwysiwygtest(request):
    return render(request, 'blogwysiwygtest.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'post_detail.html', context)
