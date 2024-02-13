from warnings import catch_warnings
from django.shortcuts import render, redirect, HttpResponse
from produits.models import Produit, Typeproduit
from produits.forms import *
from django.contrib import messages
from django.db import transaction


def Liste_produit(request):
   produits = Produit.objects.all()
   context = {
       'produits' : produits
   }
   return render(request, 'Administration/list-produits.html', context)

def View_produit(request, pk):
    produit = Produit.objects.get(id= pk)
    context = {
        'produit' : produit,
    }
    return render(request, 'Administration/details-produit.html', context)

def Update_produit(request, pk):
    produit = Produit.objects.get(id = pk)
    form = ModifierProduit(instance=produit)
    if request.method == 'POST':
        form = ModifierProduit(request.POST, instance=produit)
        form.save()
        messages.success(request,'Les informations du produit ont été modifier avec succès.')
        return redirect('produits:liste-produits')

    context = {
        'form' : form,
    }
    return render(request, 'Administration/modification-produit.html', context)

def delete_produit(request, pk):
    produit = Produit.objects.get(id= pk)
    produit.delete()
    messages.success(request, 'Le produit/article à été supprimé avec succès !')
    return redirect('produit:liste-produits')

def Create_produit(request):
    form = AjouterProduit()

    if request.method == 'POST':
        form = AjouterProduit(request.POST)
        if form.is_valid():

            reference = form.cleaned_data['reference']
            cat_produit = form.cleaned_data['cat_produit']
            designation = form.cleaned_data['designation']
            type_produit = form.cleaned_data['type_produit']
            couleur = form.cleaned_data['couleur']
            poids = form.cleaned_data['poids']
            longueur = form.cleaned_data['longueur']
            largeur = form.cleaned_data['largeur']
            hauteur = form.cleaned_data['hauteur']
            prix = form.cleaned_data['prix']
            promo = form.cleaned_data['promo']
            

            produit = Produit(
                reference = reference,
                designation = designation,
                type_produit = type_produit,
                cat_produit = cat_produit,
                couleur = couleur,
                poids = poids,
                longueur = longueur,
                largeur = largeur,
                hauteur = hauteur,
                prix = prix,
                promo = promo,
                
            )

            produit.save()
    
            messages.success(request,'La fiche produit à été créer.')
            return redirect('produits:liste-produits')

        else:
            
            messages.error(request,'Une erreur est survenu lors de la création de la fiche produit.')
            return redirect('produits:ajouter-produit')

    else:

        context = {
            'form' : form
        }

        return render(request, 'Administration/ajouter-produit.html', context)

@transaction.atomic
def StockUpdate(request, pk):
    produit = Produit.objects.get(id = pk)

    try:
        stock = Stock.objects.get(produit = produit)
    except:
        

        form = StockProduitForm()

        if request.method == 'POST':
            form = StockProduitForm(request.POST)
            if form.is_valid():
                qte = form.cleaned_data.get('qte')
                lot = form.cleaned_data.get('lot')
                date_fabrication = form.cleaned_data.get('date_fabrication')
                date_peremption = form.cleaned_data.get('date_peremption')

                stock = Stock(
                    qte = qte,
                    lot = lot,
                    date_fabrication = date_fabrication,
                    date_peremption = date_peremption,
                )
                stock.save()
                messages.success(request, 'La quantité de produit à été mise à jour.')
                return redirect("produits:liste-produits")

            else:
                messages.error(request, "Une erreure est survenue lors du traitement de l'information.")
                return redirect(request,"produits:liste-produits")

        context = {
            'produit' : produit,
            'form': form,
        }

        return render(request, 'Administration/stock-de-produit.html', context)

