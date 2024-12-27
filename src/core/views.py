from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserProfileForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator

@login_not_required
def inicio(request: HttpRequest) -> HttpResponse:
    return render(request, "core/inicio.html")

@login_not_required
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "core/index.html")

@login_not_required
def about(request: HttpRequest) -> HttpResponse:
    return render(request,"core/about.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    next_page = reverse_lazy('core:index')

@method_decorator(login_not_required, name='dispatch')
class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')

class UpdateProfileViwe(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'core/perfil.html'
    success_url = reverse_lazy('core:index') 
    def get_object(self):
        return self.request.user