from django.urls import path
from .views import (index, about, CustomLoginView, CustomRegisterView)


app_name = "core"

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register', CustomRegisterView.as_view(), name='register'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),

]