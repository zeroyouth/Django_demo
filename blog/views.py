from pydoc import render_doc
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post

# Create your views here.

def index(request):
    return HttpResponse('<h1>여기는 블로그 첫 페이지야</h1>')

def blog_post_write(request):
    if request.method == "GET":
      return render(request, 'blog/create.html')
    elif request.method == "POST":
      new_post = Post()
      new_post.title = request.POST["title"]
      new_post.content = request.POST["content"]
      new_post.save()
      return HttpResponseRedirect("/blog/post-write/")

def blog_home(request):
    blog_posts = Post.objects.all()
    print(blog_posts[0])
    context = {
        "blog_posts_key":blog_posts,
        "dummy":"나는 더미야"
    }
    return render(request,'blog/index.html', context)

def blog_post_view(request, post_id):
    a_post = Post.objects.get(id=post_id)
    context = {
        "a_post_key":a_post
    }
    return render(request, 'blog/detail.html', context)