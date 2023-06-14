from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_page,name='login'),
    path('logout',views.logoutUser, name='logout'),
    path('register',views.register,name='register'),

]
