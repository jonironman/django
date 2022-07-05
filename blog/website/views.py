from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.fds
#fdf

def welcome(request): 
    return render(request, "website/welcome.html",
                 {
                    "current_time": datetime.now(),
                    "posts": Post.objects.all(),
                    "num_posts": Post.objects.count()
                 }
    )


