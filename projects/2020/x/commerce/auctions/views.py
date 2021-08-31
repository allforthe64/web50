from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, connection
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Bid, Watchlist, Comment

CATEGORIES = {
    "MagicalItems",
    "Broomsticks",
    "MagicalFoods",
    "Miscellaneous"
}

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

    #get method
    if request.method == "GET":

        #get current user and establish message
        currentUser = request.user.username
        message = ""
        message2 = ""
        creator = False

        #get data out of listings model
        listing = Listing.objects.filter(title = listingTitle)
        
        #check to see if the page's creator is the one using the page
        if listing[0].creator == currentUser:
            creator = True

        #get comments
        comments = Comment.objects.filter(page=listingTitle)

        #get data out of bid model
        topBid = Bid.objects.filter(location = "{title}".format(title = listingTitle)).order_by('-ammount')

        if listing[0].active == False and currentUser == topBid[0].bidder:
            message = "You had the highest bid in the auction!"
        else:
            message = None

        return render(request, "auctions/listing.html", {
            "title": listingTitle,
            "description": listing[0].description,
            "image": listing[0].img, 
            "originalPrice": listing[0].beginningBid,
            "currentHighestBid": topBid[0].ammount,
            "message": message,
            "creator": creator,
            "comments": comments   

        })

    #post method
    else:

        #get data out of forms
        newBid = request.POST.get("newBid")
        watchlist = request.POST.get("watchlist")
        currentUser = request.user.username
        close = request.POST.get("close")
        creator = False
        comment = request.POST.get("commentContent")

        

        #get data out of listings model
        listing = Listing.objects.filter(title = listingTitle)

        #get data out of bid model
        topBid = Bid.objects.filter(location = "{title}".format(title = listingTitle)).order_by('-ammount')

        #get data out of comments
        comments = Comment.objects.filter(page=listingTitle)

        if listing[0].creator == currentUser:
            creator = True

        #if the user entered a bid, insert it as the new highest bid
        if newBid != None:

            #add new bid to bids table
            b = Bid(ammount=newBid, bidder=currentUser, location=listingTitle)
            b.save()

            #update highest bid of listing
            topBid = Bid.objects.filter(location = "{title}".format(title = listingTitle)).order_by('-ammount')
            Listing.objects.filter(title=listingTitle).update(highestBid = topBid[0].ammount)

            #add message 2
            message2 = "Bid saved succesfully!"

            return render(request, "auctions/listing.html", {
            "title": listingTitle,
            "description": listing[0].description,
            "image": listing[0].img, 
            "originalPrice": listing[0].beginningBid,
            "currentHighestBid": topBid[0].ammount,
            "message2": message2,
            "creator": creator,
            "comments": comments    
            
            })
        
        #add item to watchlist
        if watchlist != None:

            #add new watchlist entry to watchlist table
            w = Watchlist(page=listingTitle, watcher=currentUser)
            w.save()

            message2 = "Page succesfully added to watchlist!"

            return render(request, "auctions/listing.html", {
            "title": listingTitle,
            "description": listing[0].description,
            "image": listing[0].img, 
            "originalPrice": listing[0].beginningBid,
            "currentHighestBid": topBid[0].ammount,
            "message2": message2,
            "creator": creator,
            "comments": comments    
            
            })

        #close auction
        if close == "true":
            
            Listing.objects.filter(title=listingTitle).update(active = False)

            listing = Listing.objects.filter(title = listingTitle)

            message2 = "Auction has been closed!"

            return render(request, "auctions/listing.html", {
            "title": listingTitle,
            "description": listing[0].description,
            "image": listing[0].img, 
            "originalPrice": listing[0].beginningBid,
            "currentHighestBid": topBid[0].ammount,
            "message2": message2,
            "creator": creator,
            "comments": comments    
            
            })
            
        if comment != None:

            c = Comment(page=listingTitle, content=comment, commentor=currentUser)
            c.save()

            message2 = "Comment Posted!"

            return render(request, "auctions/listing.html", {
            "title": listingTitle,
            "description": listing[0].description,
            "image": listing[0].img, 
            "originalPrice": listing[0].beginningBid,
            "currentHighestBid": topBid[0].ammount,
            "message2": message2,
            "creator": creator,
            "comments": comments   
            
            })

        return HttpResponseRedirect(reverse("index"))


@login_required(login_url="/login")
def new(request):

    #get route
    if request.method == "GET":
        message = None
        names = ["Magical Items", "Broomsticks", "Magical Foods", "Miscellaneous"]
        return render(request, "auctions/new.html", {
            "names": names,
            "categories": CATEGORIES
        })

    else:

        #get the data
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.POST.get("image")
        category = request.POST.get("category")
        price = request.POST.get("price")
        currentUser = request.user.username
        message = "New listing created!"

        if category == "MagicalItems":
            category = "Magical Items"

        if category == "MagicalFoods":
            category = "Magical Foods"

        #create new listing
        l = Listing(title=title, description=description, beginningBid=price, img=image, category=category, active=True, creator=currentUser)
        l.save()

        
        #add new bid to bids table
        b = Bid(ammount=price, bidder=currentUser, location=title)
        b.save()

        return render(request, "auctions/new.html", {
            "message": message
        })


@login_required(login_url="/login")
def watchlist(request):

    if request.method == "GET":
        #get listings out of watchlist table
        currentUser = request.user.username
        
        listings = Watchlist.objects.all().filter(watcher = currentUser)

        return render(request, "auctions/watchlist.html", {
            "listings": listings
        })
    else:
        
        #get item to remove from watchlist
        watchElement = request.POST.get("watchElement")
        currentUser = request.user.username
        listings = Watchlist.objects.all().filter(watcher = currentUser)
        message = f"Item: {watchElement} has been removed from your watchlist."

        instance = Watchlist.objects.all().filter(page=watchElement, watcher=currentUser)
        
        #error checking
        if instance == "None":
            return render(request, "auctions/watchlist.html", {
            "listings": listings,
            "message": message
        })
        else:
            instance[0].delete()

            return render(request, "auctions/watchlist.html", {
                "listings": listings,
                "message": message
            })

def category(request):

    if request.method == "GET":
        options = CATEGORIES
        searched = False

        return render(request, "auctions/category.html", {
            "options": options,
            "searched": searched
        })
    else:

        searched = True
        category = request.POST.get("categories")

        if category == "MagicalItems":
            category = "Magical Items"
        elif category == "MagicalFoods":
            category = "Magical Foods" 

        results = Listing.objects.all().filter(active = True, category = category)

        return render(request, "auctions/category.html", {
            'searched': searched,
            "results": results
        })



        