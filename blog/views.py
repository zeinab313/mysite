from django.shortcuts import render,get_object_or_404
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    post=get_object_or_404(Post,pk=pid)
    #برای اینکه با هر بار بازدید پست موردنظر یک بازدید بخورد
    post.counted_views=post.counted_views+1
    post.save()
    contex={'post':post}
    return render(request,'blog/blog-single.html',contex)
