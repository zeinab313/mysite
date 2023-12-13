from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_view(request):
    # posts=Post.objects.filter(status=1)
    #مقایسه زمان انتشار با زمان گذشته
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    post=get_object_or_404(Post,pk=pid,published_date__lte=timezone.now(),status=1)
    #برای اینکه با هر بار بازدید پست موردنظر یک عدد به تعداد بازدید اضافه شود
    post.counted_views=post.counted_views+1
    post.save()
    contex={'post':post}
    return render(request,'blog/blog-single.html',contex)
