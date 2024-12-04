from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello world. You are at chai aur Django Home page")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("this is ABOUT Page")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Contact Us ")
    return render(request, 'website/contact.html')