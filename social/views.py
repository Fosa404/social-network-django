from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .form import PostForm, SignupForm


from .models import Post, Follow


@login_required(login_url='login')
def feed(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(
        request,
        "social/feed.html",
        context
    )


@login_required(login_url='login')
def profile(request, username):
    user = request.user
    if username and username != user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
        context = {
            'user': user,
            'posts': posts
        }
        return render(
            request,
            "social/profile.html",
            context
        )
    posts = user.posts.all()
    context = {
        'user': user,
        'posts': posts
    }
    return render(request,
                  'social/profile.html',
                  context)


@login_required(login_url='login')
def create_posts(request):
    user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.user = user
        post.save()
        return redirect('feed')
    if request.method == 'GET':
        return render(request, 'social/post.html', {'form': PostForm()})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'{username} created')
            return redirect('feed')
        messages.error(request, "Please complete the fields correctly")
    form = SignupForm()
    context = {
        "form": form
    }
    return render(request, 'form/signup.html', context)


@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def start_follow(request, username):
    follower_user = request.user
    followed_user = User.objects.get(username=username)
    follow_instance = Follow(follower_user=follower_user,
                             followed_user=followed_user)
    follow_instance.save()
    return redirect('profile', username)


@login_required(login_url='login')
def stop_follow(request, username):
    follower_user = request.user
    followed_user = User.objects.get(username=username)
    follow_instance = Follow.objects.get(
        follower_user=follower_user, followed_user=followed_user)
    follow_instance.delete()
    return redirect('profile', username)
