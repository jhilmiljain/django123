from django.shortcuts import render

def home(request):
    return render(request,'library/home.html')

def register(request):
    return render(request,'library/register.html')

