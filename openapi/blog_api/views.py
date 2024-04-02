from django.shortcuts import render
from django.http import HttpResponse
from .models  import Post

# Create your views here.



posts = [
    {'title':'просто описание 1 чувака',
     'author': 'John',
     'content': 'Smart',
     'published_at':'October 1,2022'
     },
                    
    {'title':'Описание 2 чувака',
     'author': 'John',
     'content': 'Smart',
     'published_at':'October 1,2022'}
    
]

def home(requests):
    posts = Post.objects.all()
    context = { 'posts':posts
        }
    return render(requests, 'blog_api/home.html', context)

def about(requests):
    return HttpResponse('О сайте')

def deciptikon(requests):
    return HttpResponse('deciptikon')

