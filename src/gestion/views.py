from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "gestion/index.html")

def about(request: HttpRequest) -> HttpResponse:
    return render(request,"gestion/about.html")