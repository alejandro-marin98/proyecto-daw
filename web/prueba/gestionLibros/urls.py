from django.urls import path
from gestionLibros import views

urlpatterns = [
    path('', views.showBooks, name="showBooks"),
    path('getBooks/', views.getBooks),
    path('getBooks/<str:isbn>/', views.showBookDetailsByIsbn),
    path('listas/<str:operation>/<str:username>/<str:isbn>/', views.setLista),
    path('listas/', views.setLista),
    path('misLibros/', views.misLibros),
    path('addOpinion/', views.addOpinion),
    path('searchBook/', views.searchBook),
]
