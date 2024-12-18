from django.shortcuts import render

# Create your views here.

def home2(request):
    return render(request,"home1.html")

def index2(request):
    return render(request,"index1.html")