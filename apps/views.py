from django.shortcuts import render

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def compare(request):
    return render(request,'compare.html')

def wishlist(request):
    return render(request,'wishlist.html')
# Create your views here.
