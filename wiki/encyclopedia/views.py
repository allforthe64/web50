from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect

from . import util
from wiki import *
import os
from random import choice
from markdown2 import Markdown 


#initialize pages list
pages = []
entries = "E:\William\web50\wiki\entries"

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
        mark = Markdown()

        possiblePages = ["CSS", "Django", "Git", "HTML", "Python", "The dog doin"]
        if targetPage in possiblePages:
            titleMissing = False
        else:
            titleMissing = True


        #check to see if a result was found
        if pageContent == None:
            return render(request, "encyclopedia/error.html")
        #if result was found render the page
        else:
            return render(request, "encyclopedia/Entry.html", {
                "pageContent": mark.convert(pageContent),
                "titleMissing": titleMissing,
                "title": targetPage 
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

    if request.method == "POST":
        title = request.POST.get("title")
        contents = request.POST.get("newPageContents")
        
        if util.get_entry(title) == None:
            util.save_entry(title, contents)
        
            message = "Page saved successfully!"
            return render(request, "encyclopedia/index.html", {
                "message": message
            })
        else:
            message = "An article with that title already exists!"
            return render(request, "encyclopedia/new.html",{
                "message": message
            })

#go to a random page
def random(request):
    
    #generate list to randomly go to
    
    #clear out list
    pages.clear()

    for entry in os.listdir(entries):
        
        #split off the ".md" file tag
        entry = str(entry)
        add = entry.split(".md")

        #append file name to pages list
        pages.append(add[0])

    target = choice(pages)
    return HttpResponseRedirect(f"wiki/{target}")

def edit(request, pageTitle):
    return render(request, "encyclopedia/edit.html")
