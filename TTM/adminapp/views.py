from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Admin,Register,Packages

from adminapp.models import Admin


# Create your views here.

def ttmhome(request):
    return render(request, "ttmhome.html")
def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpwd = request.POST["pwd"]

    flag =Register.objects.filter(uname=adminuname, pwd=adminpwd).values()
    if flag:
        if adminuname == "dama":
            messages.info(request, "Admin Homepage")
            return render(request, "adminhome.html")

    if flag:
        messages.info(request, "TTM Home")
        return render(request, "ttmhome.html")
    else:
        return HttpResponse("Login fail")

def checkregistration(request):
    if(request.method == "POST"):
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if(pwd==cpwd):
            if(Register.objects.filter(uname=uname).exists()):
                messages.info(request, "username exists...")
                return render(request ,"register.html")
            elif (Register.objects.filter(email=email).exists()):
                messages.info(request, "email  exists...")
                return render(request ,"register.html")
            else:
                 user = Register.objects.create(name=name,address=addr,email=email,phno=phno,uname=uname,pwd=pwd)
                 user.save()
                 messages.info(request,"user registered")
                 return render(request,"login.html")
        else:
            messages.info(request,"password doesn't match")
            return render(request,"register.html")


def checkpackages(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack=Packages.objects.create(tourcode=tcode,tourname=tname,tourpackage=tpack,desc=tdesc)
        pack.save()
        messages.info(request,"data Inserted Sucessfully")
        return render(request,"packages.html")
    else:
        messages.info(request, "Data Fail to  Inserted")
        return render(request, "packages.html")


def viewplaces(request):
    data=Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})


def checkChangePassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag = Register.objects.filter(uname=uname, pwd=opwd).values()
        if flag:
            Register.objects.filter(uname=uname, pwd=opwd).update(pwd=npwd)
            messages.info(request, "Password Updated  Sucessfully")
            return render(request, "index.html")
        else:
            return render(request,"changepassword.html")
    return render(request,"changepassword.html")

def logout(request):
    messages.info(request,"logout succesfully")
    return render(request,"login.html")


import random
import string

def random1(request):
    return render(request,'randomotp.html')

def randomotp(request):
    if request.method=="POST":
        number1=request.POST['number']
        number2=int(number1)
        results = ''.join(random.sample(string.digits,number2))
        print(results)
    return render(request,'randomotp.html',{'results':results})
