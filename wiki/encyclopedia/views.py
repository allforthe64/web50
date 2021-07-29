from django.shortcuts import render

from . import util


def index(request):
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
        return render(request, f"encyclopedia/{targetPage}.html", {
            "contents": pageContent
        })


