from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import Blogs
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.

def index(request):
    categories = Category.objects.all()
    blogs = Blogs.objects.all()
    latest = Blogs.objects.all().order_by('-pk')[:2]

    paginator = Paginator(blogs, 3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    
    try:
        blogPerpage = paginator.page(page)
    except (EmptyPage, InvalidPage):
        blogPerpage = paginator.page(paginator.num_pages)



    return render(request, "frontend/index.html", {'categories': categories, 'blogs': blogPerpage, 'latest': latest})

def blogDetail(request, id):
    singleBlog = Blogs.objects.get(id=id)
    return render(request, "frontend/blogDetail.html", {'blog': singleBlog})
