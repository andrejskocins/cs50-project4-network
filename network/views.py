from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import User, Post, Comment


def index(request):
    post_list = Post.objects.all().order_by('-datetime')
    paginator = Paginator(post_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "title": "All Posts",
        "page_obj": page_obj
    })


@login_required
def following(request):
    # Get posts from users that the current user follows
    following_users = request.user.following.all()
    post_list = Post.objects.filter(author__in=following_users).order_by('-datetime')
    paginator = Paginator(post_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "title": "Following",
        "page_obj": page_obj
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
def new_post(request):
    if request.method == "POST":
        text = request.POST.get("text-input")  # Match the form field name
        
        # Validate required fields
        if not text or text == "":
            return render(request, "network/index.html", {
                "message": "Post cannot be empty.",
                "title": "All Posts",
                "posts": Post.objects.all()
            })
        
        # Create new post with logged-in user as author
        post = Post.objects.create(
            author=request.user,
            text=text
        )

        return HttpResponseRedirect(reverse('index'))

    # If GET request, redirect to index
    return HttpResponseRedirect(reverse('index'))


def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=profile_user).order_by('-datetime')
    is_following = request.user.is_authenticated and request.user.following.filter(pk=profile_user.pk).exists()
    return render(request, "network/profile.html", {
        "profile_user": profile_user,
        "posts": posts,
        "is_following": is_following,
        "follower_count": profile_user.followers.count(),
        "following_count": profile_user.following.count()
    })

@login_required
def toggle_follow(request, username):
    profile_user = get_object_or_404(User, username=username)
    if request.user == profile_user:
        return HttpResponseRedirect(reverse('profile', args=[username]))
    
    if request.user.following.filter(pk=profile_user.pk).exists():
        request.user.following.remove(profile_user)
    else:
        request.user.following.add(profile_user)
    
    return HttpResponseRedirect(reverse('profile', args=[username]))