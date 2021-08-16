from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Bid

@login_required(login_url='/login')
def index(request):

    listings = Listing.objects.all().filter(active = True)
    links = []

    for listing in listings:
        links.append(listing.title)
    
    return render(request, "auctions/index.html", {
        "listings": listings,
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url='/login')
def listing(request, listingTitle):

    #get current user and establish message
    currentUser = request.user.username
    message = "foo"

    #get data out of listings model
    listing = Listing.objects.filter(title = listingTitle)

    #get data out of bid model
    topBid = Bid.objects.filter(location = "{title}".format(title = listingTitle)).order_by('-ammount')

    if listing[0].active == False and currentUser == topBid[0].bidder:
        message = "You had the highest bid in the auction!"

    return render(request, "auctions/listing.html", {
        "title": listingTitle,
        "description": listing[0].description,
        "image": listing[0].img, 
        "originalPrice": listing[0].beginningBid,
        "currentHighestBid": topBid[0].ammount,
        "message": message   

    })       