from django.shortcuts import render
from .views import *


def CreateCommande(request):

    

    return render(request,'templates/create_commande.html',context)
