from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('confirmation/', views.confirmation_view, name='confirmation'),
    path('participants/', views.liste_participants_view, name='liste_participants'),
]
