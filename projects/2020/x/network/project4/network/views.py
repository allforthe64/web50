import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
import datetime
from django.views.decorators.csrf import csrf_exempt


from .models import User, Entry, Follow

def index(request):
    
    #get all of the entries out of the database
    allPosts = Entry.objects.all().order_by("-timestamp")

    #set up paginator object
    paginator = Paginator(allPosts, 10)
    pageNumber = request.GET.get('page')
    pageObject = paginator.get_page(pageNumber)
    
    return render(request, "network/index.html", {
        "posts": pageObject
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


def new(request):
    
    #get route
    if request.method == "GET":
        return render(request, "network/post.html")
    
    #post route
    else:
        
        #establish variables
        content = request.POST.get("postContent")
        user = request.user
        
        #create new object
        entry = Entry(content=content, poster=user)
        entry.save()

        messages.add_message(request, messages.SUCCESS, "Posted!")

        return HttpResponseRedirect(reverse('index'))

# like function and unlike
@csrf_exempt
@login_required
def like(request, post_id):
    
    #query for requested post
    try:
        entry = Entry.objects.get(post_id=post_id)
    except Entry.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    #return post contents
    if request.method == "GET":
        return JsonResponse(entry.serialize())

    #update posts likes
    elif request.method == "PUT":
        data = json.loads(request.body)
        if data.get("likes") is not None:
            entry.likes = data["likes"]

        # save the updated object
        entry.save()
        return HttpResponse(status=204)

    #request must be get or put
    else:
        return JsonResponse({
            "error": "GET or PUT request required"
        }, status=400)

# view profile function
def profile(request, username):

    followers = Follow.objects.all().filter(following=username)
    following = Follow.objects.all().filter(followedBy=username)

    return render(request, "network/profile.html", {
        "username":request.user.username,
        "viewing": username,
        "followers": len(followers),
        "following": len(following)   
    })

# follow/unfollow function
@csrf_exempt
@login_required
def follow(request, action, account):

    data = json.loads(request.body)
    
    # create a new follower object
    if action == "follow":
        f = Follow(following=data["following"], followedBy=data["followedBy"])
        f.save()

        return HttpResponse(status=204)
    
    #delete a follower
    else:

        Follow.objects.filter(following=data["following"], followedBy=data["followedBy"]).delete()

        return HttpResponse(status=204)

@csrf_exempt
@login_required
def search(request):

    data = json.loads(request.body)

    #query the database to see if the current user has already followed

@csrf_exempt
@login_required
def number(request, target):

    #query the database 
    f = Follow.objects.filter(following=target)

    return JsonResponse(len(f), safe=False)
