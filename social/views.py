from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404
from .form import PostForm, SignupForm, ProfileForm
from .models import Profile


from .models import Post, Follow


@login_required(login_url='login')
def feed(request):
    current_user = request.user
    if request.method == 'GET':
        following_users_ids = Follow.objects.filter(
            follower_user=current_user).values_list('followed_user_id', flat=True)
        posts = Post.objects.filter(user_id=current_user.id)
        posts |= Post.objects.filter(user_id__in=following_users_ids)
        context = {
            "posts": posts
        }
        return render(
            request,
            "social/feed.html",
            context
        )
    if request.method == 'POST':
        search_user = User.objects.filter(
            username__contains=request.POST.get('search_users'))
        try:
            user = get_object_or_404(search_user)
            return redirect('profile', user.username)
        except Http404:
            messages.error(request, 'No user found with that username')
        return redirect('feed')


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
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        instance = get_object_or_404(Profile, user_id=user.id)
        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
        messages.error(request, 'upload a correct image type')
    if request.method == 'GET':
        form = ProfileForm()
        context = {
            'user': user,
            'form': form
        }
        return render(request,
                      'form/update_profile.html',
                      context)


@ login_required(login_url='login')
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
            password = form.cleaned_data['password1']
            messages.success(request, f'{username} created')
            user = authenticate(request, username=username, password=password)
            login(request, user=user)
            return redirect('feed')
        messages.error(request, "Please complete the fields correctly")
    form = SignupForm()
    context = {
        "form": form
    }
    return render(request, 'form/signup.html', context)


@ login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('login')


@ login_required(login_url='login')
def start_follow(request, username):
    follower_user = request.user
    followed_user = User.objects.get(username=username)
    follow_instance = Follow(follower_user=follower_user,
                             followed_user=followed_user)
    follow_instance.save()
    return redirect('profile', username)


@ login_required(login_url='login')
def stop_follow(request, username):
    follower_user = request.user
    followed_user = User.objects.get(username=username)
    follow_instance = Follow.objects.get(
        follower_user=follower_user, followed_user=followed_user)
    follow_instance.delete()
    return redirect('profile', username)
