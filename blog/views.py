from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_view(request,**kwargs):
    # posts=Post.objects.filter(status=1)
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if kwargs.get('cat_name'):
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('authoer_username'):
        posts=posts.filter(author__username=kwargs['author_username'])
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    post=get_object_or_404(Post,pk=pid,published_date__lte=timezone.now(),status=1)
    # post_prev=get_object_or_404(Post,pk=pid-1,published_date__lte=timezone.now(),status=1)
    post.counted_views=post.counted_views+1
    post.save()
    contex={'post':post}
    return render(request,'blog/blog-single.html',contex)

def blog_category(request,cat_name):
    posts=Post.objects.filter(status=1)
    posts=posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    # posts=Post.objects.filter(status=1)
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if request.method=='GET':
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
