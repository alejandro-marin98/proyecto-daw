from django.urls import path
from login import views

urlpatterns = [
    path('', views.loginUser),
    path('logout/', views.cerrarSesion),    
    path('signup/', views.createUser),
]
