from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "core/index.html")

def about(request: HttpRequest) -> HttpResponse:
    return render(request,"core/about.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    next_page = reverse_lazy('core:index')

class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')