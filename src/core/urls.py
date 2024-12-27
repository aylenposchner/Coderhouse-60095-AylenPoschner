from django.urls import path
from .views import (inicio, index, about, CustomLoginView, CustomRegisterView, UpdateProfileViwe)
from django.contrib.auth.views import LogoutView


app_name = "core"

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', UpdateProfileViwe.as_view(), name='perfil'),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name='logout'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),

]