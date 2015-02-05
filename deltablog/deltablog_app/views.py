from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'deltablog_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'deltablog_app/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.image = request.FILES['image']
            post.save()
            return redirect('deltablog_app.views.post_detail', pk=post.pk)
            #posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
            #return render(request, 'deltablog_app/post_list.html', {'posts': posts})
    else:
        form = PostForm()
    return render(request, 'deltablog_app/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('deltablog_app.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'deltablog_app/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'deltablog_app/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    #return redirect('deltablog_app.views.post_detail', pk=pk)
    return post_list(request)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    posts = Post.objects.filter(published_date__isnull=True)
    if Post.objects.filter(published_date__isnull=True).exists():
        return post_draft_list(request)
    else:
        return redirect('deltablog_app.views.post_list')
