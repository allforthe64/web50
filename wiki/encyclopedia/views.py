from django.shortcuts import render
from django.shortcuts import redirect

from . import util
from wiki import *
import os


#initialize pages list
pages = []
entries = "/Users/linds/Desktop/will/web50/web50/wiki/entries"

def index(request):

    #clear out list
    pages.clear()

    for entry in os.listdir(entries):
        
        #split off the ".md" file tag
        entry = str(entry)
        add = entry.split(".md")

        #append file name to pages list
        pages.append(add[0])


    #search list of entries for page
    if request.method == "POST":
        query = request.POST.get("q")
        
        if query in pages:
            return redirect(f"wiki/{query}")
        else:

            #iterate over each entry in the page and check if substring in entry
            print(pages)
            for page in pages:
                if query in page:
                    print(page)
                    print("Found!")

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


