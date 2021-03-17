from django.shortcuts import render, redirect
from .models import Dojo, Ninja 

# Create your views here.

def index(request):
    # print(Dojo.objects.all())
    context = {"all_dojos": Dojo.objects.all(), "message": "Hewwo World"}
    return render(request, "index.html", context)


def people(request):
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST["last_name"],
        dojo_id = request.POST["dojo_id"]
    )
    print(request.POST)
    # print(f"NEW USER ID: {students.id}")
    return redirect("/")

def building(request):
    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state']
    )
    return redirect("/")