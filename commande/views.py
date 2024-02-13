from django.shortcuts import render
from .models import *



def ListCommandes(request):
    commandes= CommandeFournisseur.objects.all()
    context={
        'commandes' : commandes,
    }
    return render(request, 'Administration/list-commandes.html', context)

def AjouterCommande(request):
    return render(request, 'Administration/creer-une-commande.html')

def DetailsCommande(request):
    return render(request, 'Administration/details-commande.html')

def SupprimerCommande(request):
    pass
