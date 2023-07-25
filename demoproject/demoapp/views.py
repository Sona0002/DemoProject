from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#
def demo(request):
    return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("Please check in the details page")
#
# def details(request):
#     return render(request,"details.html")
#
# def thanks(request):
#     return HttpResponse("Thankyou!!!")

def operation(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res1=x+y
    res2=x-y
    res3=x*y
    res4=x//y
    return render(request,"result.html",{'add':res1,'sub':res2,'mul':res3,'div':res4})

