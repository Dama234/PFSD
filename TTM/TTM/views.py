from django.shortcuts import render


def homePage(request):
    return render(request,'index.html')



def loginPage(request):
    return render(request,'login.html')

def registrationpage(request):
    return render(request, "register.html")

def viewpackages(request):
    return render(request,'viewpackages.html')

def insertpackages(request):
    return render(request,'insertpackages.html')

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
