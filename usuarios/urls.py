from django.contrib import admin
from django.urls import path
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    path('registrar', RegistrarUsuarioView.as_view(), name='registrar'),
    path('login/', login, {'template_name':'login.html'}, name='login'),
    path('logout/', logout_then_login, {'login_url':'/login/'}, name='logout')
]