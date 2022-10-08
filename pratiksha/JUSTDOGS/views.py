from django.shortcuts import render,redirect
from .models import Justdogs,Order
from django.contrib import messages

def home(request):
    data =  Justdogs.objects.all()
    return render(request,"home.html",{"data":data})

def buy(request,id):
    justdogs = Justdogs.objects.get(id=id)
    return render(request, "buy.html",{"justdogs":justdogs})


def placeOrder(request):
    o= Order()
    o.dogname = request.POST.get("justdogs")
    o.name = request.POST.get("name")
    o.email = request.POST.get("email")
    o.address= request.POST.get("address")
    o.number = request.POST.get("mobile")

    o.save()
    messages.success(request,"ordered placed")
    return redirect("/home")

