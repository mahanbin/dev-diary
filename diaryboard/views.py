from django.shortcuts import render,redirect
from django.contrib import auth
from .models import Post
from django.conf import settings
from .forms import postForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def boardview(request):

    posts = Post.objects.all()
    print('posts :',posts)
    context = {
        'posts': posts
    }
    return render(request,'boardview.html',context)

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
