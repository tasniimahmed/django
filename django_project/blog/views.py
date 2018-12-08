from django.shortcuts import render
from .models import post
#posts is a list od dictionaries


def home (request):
    context = {
        'posts': post.objects.all()
    }
    #render to return http response
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})