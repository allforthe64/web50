from django.shortcuts import render

from . import util
from wiki import *


#initialize pages list
pages = ["CSS", "Django", "Git", "HTML", "Python"]

def index(request):

    #search list of entries for page
    if request.method == "POST":
        query = request.POST.get("q")

        if query == "Sbeve":
            return render(request, "encyclopedia/error.html")

        else:
            return render(request, "encyclopedia/index.html")

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, targetPage):
    #search for .md file and get its contents
    pageContent = util.get_entry(targetPage)

    #check to see if a result was found
    if pageContent == None:
        return render(request, "encyclopedia/error.html")
    #if result was found render the page
    else:
        return render(request, f"encyclopedia/Entry.html", {
            "contents": pageContent,
            "pageTitle": targetPage
        })


