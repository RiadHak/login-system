from django.urls import path, include
from . import views
urlpatterns = [
    path('home',views.home),
    path('login',views.login),
    path('register',views.register),

]
