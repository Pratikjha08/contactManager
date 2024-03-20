from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

contacts = dict()

def index(request):
    sorted_contacts = dict(sorted(contacts.items()))
    return render(request, "contact/index.html", {
        "sorted_contacts":sorted_contacts
    })

def add(request):
    return render(request, "contact/add.html")

def save_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phnumber = request.POST['phnumber']
        if name and phnumber:
            new_data = {name:phnumber}
            contacts.update(new_data)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "contact/add.html", {
                "name":name,
                "phnumber":phnumber
            })