from django.shortcuts import render

# Create your views here.
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
