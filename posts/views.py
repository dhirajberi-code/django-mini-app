from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'index.htm', {'posts': posts})

def add(request):
    form = PostForm()
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': form, "posts":posts}
            return render(request, 'blogform.htm', context)

    return render(request, 'blogform.htm', {'form': form, "posts":posts})

def update(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form":form}
    return render(request, 'update.htm', context)

def delete(request, pk):
    post = Post.objects.get(id=pk)    
    post.delete()
    return redirect('/')