from django.db import models


CAT_PRD={
    ('srv' , 'Service'),
    ('prd', 'Produits'),
}


class Typeproduit(models.Model):
    designation = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.designation

class Produit(models.Model):
    reference = models.CharField(max_length=1000, null=True, blank=True)
    designation = models.CharField(max_length=1000, null=True, blank=True)
    type_produit = models.ForeignKey(Typeproduit, null=True, blank=True, on_delete=models.CASCADE)
    cat_produit = models.CharField(max_length=3, null=True, blank=True, choices=CAT_PRD)

    #détails du produit
    couleur = models.CharField(max_length=100, null=True, blank=True)
    poids = models.FloatField(null=True, blank=True)
    longueur = models.FloatField(null=True, blank=True)
    largeur = models.FloatField(null=True, blank=True)
    hauteur = models.FloatField(null=True, blank=True)
    
    #tarification du produit
    prix = models.FloatField(null=True, blank=True)
    promo = models.FloatField(null=True, blank=True)

    image = models.ImageField(null=True, blank=True)

    id_company = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name='Produit'
        verbose_name_plural='Produits'

    def __str__(self):
        return self.designation

class Stock(models.Model):
    produit = models.OneToOneField(Produit, null=True, blank=True,on_delete=models.DO_NOTHING)
    qte = models.FloatField(null=True, blank=True)
    lot = models.CharField(max_length=100, null=True, blank=True)
    date_fabrication = models.DateField(null=True, blank=True)
    date_peremption  = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Stock produit"
        verbose_name_plural="Stock de produits"

    def __str__(self):
        return self.produit

TYPE_OPERATION = {
    ('s', 'Sortie'),
    ('e', 'Entrer'),
}

class MouvementStock(models.Model):
    produit = models.ForeignKey(Produit, null=True, blank=True, on_delete=models.DO_NOTHING)
    date_operation = models.DateTimeField(null=True, blank=True)
    type_operation = models.CharField(max_length=2, null=True, blank=True, choices=TYPE_OPERATION)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Mouvement de stock"
        verbose_name_plural="Mouvements de stock"
    
    def __str__(self):
        return self.produit



    




