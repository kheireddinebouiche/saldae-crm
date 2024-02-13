from statistics import mode
from tkinter import N
from django.db import models
from produits.models import Produit
from leads.models import Lead
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from leads.models import User
from leads.models import Fournisseurs





class LigneDeCommande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    prix = models.FloatField(null=True, blank=True)

    is_done = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Ligne de commande'
        verbose_name_plural='Lignes de commandes'

    def __str__(self):
        return self.item.designation

       

class CommandeFournisseur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(LigneDeCommande)
    total = models.FloatField(null=True, blank=True)

    is_done = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Commande de produit'
        verbose_name_plural='Commandes de produits'

    def __str__(self):
        return self.user.username




