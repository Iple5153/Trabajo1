from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path(r'', views.home),
    path(r'login/', LoginView.as_view(), name='Iniciar'),
    path(r'logout/', LogoutView.as_view(), name='Cerrar Seccion'),
    path(r'register/', views.register, name='Registrarse'),
]