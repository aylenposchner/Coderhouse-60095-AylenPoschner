from django.shortcuts import render

def index(request):
    return render(request, "gestion/index.html")

def about(request):
    return render(request,"gestion/about.html")