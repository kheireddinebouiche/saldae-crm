from django.db import models
from produits.models import Produit
from leads.models import Lead
from django.dispatch import receiver
from django.template.defaultfilters import slugify



PAIEMENT = {
    ('atr', 'A terme'),
    ('30j', '30 Jours'),
    ('40j', '40 Jours'),
    ('60j', '60 Jours'),
    
}

STATUS = {
    ('att', 'En attente'),
    ('con', 'Confirmer'),
    ('val', 'Valider'),
    ('ann', 'Annuler'),
}

class LigneBonCommande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.produit.reference

def increment_order_id():
        dernier_order = BonDeCommande.objects.all().order_by('id').last()
        if not dernier_order:
            return 'Bon de commande N° :/' + '1'
        id_commande = dernier_order.id_commande
        item_order_nb = int(id_commande.split('Bon de commande N° :/')[-1])
        n_item_order_nb = item_order_nb + 1
        n_item_order_id = 'Bon de commande N° :/' + str(n_item_order_nb)
        return n_item_order_id

class BonDeCommande(models.Model):
    id_commande = models.CharField(max_length=1000,default=increment_order_id, null=True, blank=True)
    date_commande = models.DateField()
    adresse_livraison = models.CharField(max_length=1000, null=True, blank=True)
    observation = models.CharField(max_length=1000, null=True, blank=True)
    delai_paiement = models.CharField(max_length=3, choices=PAIEMENT, null=True, blank=True)
    ligne_commande = models.ManyToManyField(LigneBonCommande)
    client = models.ForeignKey(Lead, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS, null=True, blank=True)
    
    def __str__(self):
        return self.id_commande

