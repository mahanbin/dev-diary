from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from .models import Post
from django.conf import settings
from .forms import postForm
from django.core.paginator import Paginator

all_posts = Post.objects.all()

# Create your views here.
def index(request):
    return render(request,'index.html',{'posts':all_posts})

def boardview(request):
    posts = all_posts.order_by('-id')
    paginator = Paginator(posts,7)
    page = request.GET.get('page')
    context = {
        'posts': posts,
        'pages': paginator.get_page(page)
    }
    return render(request,'boardview.html',context)

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request,'detail.html',{'post':post_detail})

def boardwrite(request):
    form = postForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            Post.objects.create(
                author= auth.get_user_model().objects.get(username='hanbin'),
                title= form.cleaned_data['title'],
                content= form.cleaned_data['content']
            )
        return redirect('boardview')
    else:
        return render(request,'boardwrite.html',{'form':form})

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = postForm(request.POST, instance=post)
        form.save()
        return render(request,'detail.html',{'post':post})

    form = postForm(instance=post)
    return render(request,'boardupdate.html',{'form':form,'post':post})


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('boardview')
