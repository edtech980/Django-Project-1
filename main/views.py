from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateNewPost
from main.models import BloggerList
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(response):
    posts = BloggerList.objects.all()
    if response.method == "POST":
        for post in posts:
            if response.POST.get(str(post.id)):
                del_object = BloggerList.objects.get(id=post.id)
                del_object.delete()
                posts = BloggerList.objects.all()
                return redirect("/")
                # return render(response, "blogger/home.html", {"posts": posts})
            else:
                print()

    """
    now = datetime.now()
    d1 = now.strftime("%d %B %Y   %H:%M:%S")
    print(d1)

    newpost = BloggerList(
        title="Software Engineer", text="Life as a developer is Hard, You need to sweat and bleed", time_post=d1)
    newpost.save()
    """
    return render(response, "main/home.html", {"posts": posts, "count": len(posts)})


def posts(response):
    return render(response, "main/posts.html", {})


def post(response):
    return render(response, "main/post.html", {})


def newpost(response):
    newpost_form = CreateNewPost()
    now = datetime.now()
    d1 = now.strftime("%d %B %Y   %H:%M:%S")
    print("Inside New post")
    if response.method == "POST":
        print("Entering")
        form = CreateNewPost(response.POST)
        if form.is_valid():
            post_title = form.cleaned_data["title"]
            post_text = form.cleaned_data["post"]

            post = BloggerList(title=post_title, text=post_text, time_post=d1)
            post.save()
            response.user.bloggerlist.add(post)
            print("Saved")

            #posts = BloggerList.objects.all()
            # return render(response, "blogger/home.html", {"posts": posts})
            return redirect("/")
        else:
            form = CreateNewPost()
    return render(response, "main/newpost.html", {"newpost_form": newpost_form})


def login(response):

    return render(response, "main/login.html", {})


def logout(response):
    return render(response, "main/logout.html", {})


def signup(response):

    return render(response, "main/signup.html", {})
