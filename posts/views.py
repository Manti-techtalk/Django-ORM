from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def posts(request):
    return render(request,'posts/posts.html')