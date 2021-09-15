from django.shortcuts import render
from .models import Post
# Create your views here.
def hello(request):
    #Query data from model
    data = Post.objects.all()
    return render(request, 'index.html', {'posts':data})

def page1(request):
    return render(request, 'page1.html')

def createForm(request):
    return render(request, 'form.html')

def addBlog(request):
    name = request.POST['name']
    description = request.POST['description']
    return render(request, 'result.html',
        {
            'name': name,
            'description': description

        }
    )

