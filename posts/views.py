from django.shortcuts import render
from django.http import HttpRequest
from .models import Posts

# Create your views here.
def posts(request):
    posts = Posts.objects.all().order_by('-date')
    return render(request,'posts/posts.html',{'posts':posts})