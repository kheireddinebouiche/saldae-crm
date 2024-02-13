from decimal import Decimal
from numbers import Number
from tokenize import Floatnumber
from django.forms import ModelForm, widgets
from produits.models import *
from django import forms



CAT_PRD={
    ('srv' , 'Service'),
    ('prd', 'Produits'),
}

class AjouterProduit(forms.ModelForm):
    
    class Meta:
        model = Produit
        fields = (
            "reference",
            "designation",
            "type_produit",
            "cat_produit",
            "couleur",
            "poids",
            "longueur",
            "largeur",
            "hauteur",
            "prix",
            "promo",
            "image",
        )

        widgets = {
            'reference' : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Référence du produit'
            }),
            "designation" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Désignation du produit',
                'label' : 'Libellé/Désignation'
            }),
            "prix" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Prix',
            }),
            "promo" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Promotion'
            }),

            "largeur" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Largeur',
            }),

            'longeur' : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Longeur',
            }),

            "hauteur" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Hauteur',
            }),

            "couleur" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Couleur',
            }),

            "poids" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Poid',
            }),
            "cat_produit" : widgets.Select(attrs={
                'class' : 'form-control',
                'choices' : 'CAT_PRD'
            }),
            "type_produit" : widgets.Select(attrs={
                'class' : 'form-control',
                
            }),
        }

class ModifierProduit(forms.ModelForm):  
    class Meta:
        model = Produit
        fields = ("reference","designation","type_produit","cat_produit","couleur","poids","longueur","largeur","hauteur",
            "prix",
            "promo",
            "image",
        )

        widgets = {
            'reference' : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Référence du produit'
            }),
            "designation" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Désignation du produit',
                'label' : 'Libellé/Désignation'
            }),
            "prix" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Prix',
            }),
            "promo" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Promotion'
            }),

            "largeur" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Largeur',
            }),

            'longeur' : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Longeur',
            }),

            "hauteur" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Hauteur',
            }),

            "couleur" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Couleur',
            }),

            "poids" : widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Poid',
            }),
            "cat_produit" : widgets.Select(attrs={
                'class' : 'form-control',
                'choices' : 'CAT_PRD'
            }),
            "type_produit" : widgets.Select(attrs={
                'class' : 'form-control',
                
            }),
        }

class StockProduitForm(ModelForm):
    class Meta:
        model = Stock
        fields = {'qte','lot','date_fabrication','date_peremption'}
        widgets = {
            'qte': widgets.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Quantité de produit'
            }),
            'lot': widgets.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'N° de Lot'
            }),
            'date_fabrication' : widgets.DateInput(attrs={
                'class' : 'form-control',
            }),
            'date_peremption' : widgets.DateInput(attrs={
                'class': 'form-control',
                
            }),
        }