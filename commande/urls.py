from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name="commande"

urlpatterns = [
    path('list-des-commandes/', ListCommandes, name="list-commandes"),
    path('details-commande/', DetailsCommande, name="details-commande"),
    path('ajouter-commande/', AjouterCommande, name='ajouter-commande'),
]
