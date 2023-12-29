from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.utils import timezone
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def blog_view(request,**kwargs):
    # posts=Post.objects.filter(status=1)
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if kwargs.get('cat_name'):
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('authoer_username'):
        posts=posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name'):
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])
    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'save comment seccessfully')
        else:
            messages.add_message(request,messages.ERROR,'dont save comment')

   
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    post=get_object_or_404(posts,pk=pid,published_date__lte=timezone.now(),status=1)
    post.counted_views=post.counted_views+1
    post.save()
    post_next=posts.filter(id__gt=post.id).order_by('id').first()
    post_prev= posts.filter(id__lt=post.id).order_by('-id').first()
    if post.login_require:
        comments=Comment.objects.filter(post=post.id,approved=True)
        form=CommentForm()
        contex={'post':post, 'post_next':post_next,'post_prev':post_prev,'comments':comments,'form':form}
        # contex={'post':post}
        return render(request,'blog/blog-single.html',contex)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))
    

    

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
