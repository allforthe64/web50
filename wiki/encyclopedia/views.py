from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect

from . import util
from wiki import *
import os


#initialize pages list
pages = []
entries = "/Users/linds/Desktop/will/web50/web50/wiki/entries"

#initalize list to hold search entries
relatedEntries = []

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
            #clear related entries list
            relatedEntries.clear()

            #iterate over each entry in the page and check if substring in entry
            for page in pages:
                if query in page:
                    relatedEntries.append(page)

            return render(request, "encyclopedia/related.html",{
                "entries": relatedEntries
            })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, targetPage):
    
    if request.method == "GET":
        
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
    else:
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
                print(query)
                return HttpResponseRedirect(f"{query}")
            else:
                #clear related entries list
                relatedEntries.clear()

                #iterate over each entry in the page and check if substring in entry
                for page in pages:
                    if query in page:
                        relatedEntries.append(page)

                return render(request, "encyclopedia/relatedPage.html",{
                    "entries": relatedEntries
                })

#create a new page
def new(request):

    if request.method == "GET":
        return render(request, "encyclopedia/new.html")


