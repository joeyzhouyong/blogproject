from django.shortcuts import render,get_list_or_404
from .models import Post

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request,pk):
    post = get_list_or_404(Post,pk=pk)
    return render(request,'blog/detail.html',context={'post':post})