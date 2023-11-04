from django.shortcuts import render
from . import util
import markdown2
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/error.html",{
            "message" : "Error: Requested page not found."
        })
    else :
        return render(request, "encyclopedia/entry.html",{
            "title" : title,
            "content" : markdown2.markdown(util.get_entry(title))
        })

def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title= request.POST['title']
        content = request.POST['content']
        existing_title = util.get_entry(title)
        if existing_title is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Page already exists"
            })
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                'content': markdown2.markdown(util.get_entry(title))
            })
        
def search(request):
    if request.method == "POST":
        query = request.POST['q']
        content = util.get_entry(query)
        if content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title" : query,
                "content": markdown2.markdown(util.get_entry(query))
            })
        else:
            entries = util.list_entries()
            suggestion = [entry for entry in entries if query.lower() in entry.lower()]
            return render(request, "encyclopedia/search.html", {
                "suggestion": suggestion
            })
        
def edit(request):
    if request.method == "POST":
        title= request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title" : title,
            "content" : content
        })
    
def submitChanges(request):
    if request.method =="POST":
        title= request.POST['title']
        content= request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "content": markdown2.markdown(util.get_entry(title))
        })


def randomPage(request):
    entries= util.list_entries()
    random_entry = random.choice(entries)
    return render(request, "encyclopedia/entry.html", {
        "title" : random_entry,
        "content" : markdown2.markdown(util.get_entry(random_entry))
    })