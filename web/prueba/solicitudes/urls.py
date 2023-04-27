from django.urls import path
from solicitudes import views

urlpatterns = [
    path('', views.showSolicitudes),
    path('responder/', views.responder),
    path('mandar_solicitud/', views.mandar_solicitud),
]
