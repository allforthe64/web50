from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, targetPage):
    return render(request, f"encyclopedia/{targetPage}.html", {
        "contents": util.get_entry(targetPage)
    })


