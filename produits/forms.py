from django.forms import ModelForm, widgets
from produits.models import Produit
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

