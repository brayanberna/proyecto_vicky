from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/registro', views.register, name='register'),
    path('usuarios/logout', views.logout_view, name='logout'),
]
