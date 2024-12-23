from django.urls import path
from .views import (index, about, CustomLoginView, CustomRegisterView)
from django.contrib.auth.views import LogoutView


app_name = "core"

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register', CustomRegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name='logout'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),

]