
from django.contrib import admin
from django.urls import path
from produits.views import *

app_name="produits"

urlpatterns = [
    
    path('Administration/produits/ajouter-produit/', Create_produit, name="ajouter-produit"),
    path('Administration/produit/liste-produits/', Liste_produit , name="liste-produits"),
    path('Administration/produit/details-produit/<int:pk>/', View_produit , name="details-produit"),
    path('<int:pk>/Administration/produit/modification-produit/', Update_produit , name="modification-produit"),
    path('<int:pk>/supprimer-produit/',delete_produit, name="delete-produit"),
     
]