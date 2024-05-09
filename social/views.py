from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .form import PostForm, SignupForm


from .models import Post


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


def create_posts(request):
    user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.user = user
        post.save()
        return redirect('feed')
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


def log_out(request):
    logout(request)
    return redirect('login')
