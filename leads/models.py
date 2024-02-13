from re import T
from tkinter import N
from tkinter.tix import Tree
from turtle import update
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import DO_NOTHING, SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from produits.models import Produit
from django.db.models import Q


SOURCE_CHOICES = {
        ('Youtube', 'Youtube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    }

USER_TYPE = {
    ('ve', 'Vendeur'),
    ('ag', 'Agent'),
    ('ad', 'Administrateur'),
}

NOTE_STATUS = {
    ('act', 'Active'),
    ('enc', 'En cours'),
}

class User(AbstractUser):
    pass

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_identification = models.CharField(max_length=100, null=True, blank = True)
    user_type = models.CharField(max_length=2, choices=USER_TYPE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    tel = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=100, null=True, blank=True)

    id_company = models.IntegerField(null=True, blank=True)
    has_company = models.BooleanField(default=False, null=True, blank=True)

    lim_note = models.IntegerField(null=True, blank=True)
    lim_client = models.IntegerField(null=True, blank=True)
    lim_fournisseur = models.IntegerField(null=True, blank=True)
    

    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_agent(sender, instance, created, **kwargs):
        if created:
            Agent.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_agent(sender, instance, **kwargs):
        instance.agent.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.num_identification)
        super(Agent, self).save(*args, **kwargs)

class Lead(models.Model):

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    phoned = models.BooleanField(default = False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100, null=True, blank=True)

    profile_picture = models.ImageField(blank=True, null=True)

    special_files = models.FileField(null=True, blank=True)


    def __str__(self):
        return self.first_name

CAT_CLIENT = {
    ('p', 'Personne'),
    ('e', 'Entreprise'),
}

TYPE_CLIENT = {
    ('pr', 'Prospet'),
    ('Fr', 'Fournisseur'),
    ('cl', 'Client'),
}

RDV_STATUS={
    ('con', 'Confirmé'),
    ('ann', 'Annulé'),
    ('att', 'En attante')
    
}

class Client(models.Model):
    raison = models.CharField(max_length=100, null=True, blank=True)

    num = models.IntegerField(null=True, blank=True)

    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)

    adresse = models.CharField(max_length=1000, null=True, blank=True)
    rue = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    pays = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=100, null=True, blank=True)

    gerant = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=12, null=True, blank=True)
    fax = models.CharField(max_length=14, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    nrc = models.CharField(max_length=50, null=True, blank=True)
    nif = models.CharField(max_length=50, null=True, blank=True )
    art = models.CharField(max_length=50, null=True, blank=True)

    categorie_client = models.CharField(max_length=1, choices=CAT_CLIENT, null=True, blank=True)
    type_client = models.CharField(max_length=2, choices=TYPE_CLIENT, null=True, blank=True)
    secteur = models.ForeignKey('SecteurActivite', null=True, blank=True, on_delete=models.CASCADE)

    id_comp = models.IntegerField(null=True, blank=True)

    created_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name="Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.raison

class RendezVous(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    date_rendez_vous = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=3, choices=RDV_STATUS, null=True, blank=True)
    motif = models.CharField(max_length=100, null=True, blank=True)
    observation = models.TextField(max_length=1000, null=True, blank=True)

    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    id_comp = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Rendez vous",
        verbose_name_plural = "Liste des rendez vous"

    def __str__(self):
        return self.client.raison

TYPE_FOURNISSEUR = {
    ('pa', 'Paticulier'),
    ('en', 'Entreprise'),
}

class SecteurActivite(models.Model):
    libelle = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name="Secteur"
        verbose_name_plural = "Secteurs"

    def __str__(self):
        return self.libelle

class Fournisseurs(models.Model):
    raison = models.CharField(max_length=1000, null=True, blank=True)
    secteur = models.ForeignKey(SecteurActivite, null=True, blank=True, on_delete=models.DO_NOTHING)

    num = models.IntegerField(null=True, blank=True)

    adresse = models.TextField(max_length=2000, null=True, blank=True)
    pays = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=100, null=True, blank=True)
    rue = models.CharField(max_length=100, null=True, blank=True)

    mobile = models.CharField(max_length=13, null=True, blank=True)
    telephone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    fournisseur_type = models.CharField(max_length=2, choices=TYPE_FOURNISSEUR, )
    image = models.ImageField(null=True, blank=True)

    id_comp = models.IntegerField(null=True, blank=True)

    nis = models.CharField(max_length=300, null=True, blank=True)
    nif = models.CharField(max_length=100, null=True, blank=True)
    art = models.CharField(max_length=100, null=True, blank=True)
    rc = models.CharField(max_length=100, null=100, blank=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name="Fournisseur"
        verbose_name_plural="Fournisseurs"

    def __str__(self):
        return self.raison

STATUS_DEVIS=  {
    ('env', 'Envoyé'),
    ('acc', 'Accepté'),
    ('Ter', 'Terminé'),
    ('fac', 'Facturé'),
    ('ann', 'Annullé'),
}

MODE_PAIEMENT ={
    ('Virement', 'Virement'),
    ('Cash', 'Cash'),
    ('Terme', 'A terme'),
}

ETAT = {
    ('enc', 'En cours'),
    ('rep', 'Pause'),
    ('bro', 'Brouillon'),
    ('sau', 'Sauvegarder'),
}

class Devis(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=SET_NULL)
    num_client = models.CharField(max_length=1000, blank=True, null=True)
    num = models.IntegerField(null=True, blank=True)
    prospet = models.ForeignKey('Client', null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_DEVIS, null=True, blank=True)
    lignes_devis = models.ManyToManyField('ProduitsDevis', blank=True)
    observation = models.TextField(max_length=100, null=True, blank=True)
    date_du_bon = models.DateField(null=True, blank=True)
    adresse_livraison = models.CharField(max_length=1000, null=True, blank=True)
    methode_paiement = models.CharField(max_length=10, null=True, blank=True, choices=MODE_PAIEMENT)

    etat = models.CharField(max_length=3, null=True, blank=True, choices=ETAT)

    montant_tva = models.FloatField(null=True, blank=True)
    sous_total = models.FloatField(null=True, blank=True)
    total_devis = models.FloatField(null=True, blank=True)

    created_at= models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)

    id_comp = models.IntegerField(null = True, blank=True)

    class Meta:
        verbose_name="Devis"
        verbose_name_plural="Devis"

    def __str__(self):
        return self.prospet.raison

class ProduitsDevis(models.Model):
    product = models.ForeignKey(Produit, null=True, blank=True, on_delete=DO_NOTHING)
    reference_product = models.CharField(max_length=100, null=True, blank=True)
    qtr = models.IntegerField(null=True, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    remise = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Ligne de devis'
        verbose_name_plural ='Lignes de devis'

    def __str__(self):
        return self.product.designation

   # @property
   # def save(self):
    #    total = self.qtr * self.product.prix
    #    return total

class Note(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 

    num = models.IntegerField(null=True, blank=True)

    titre = models.CharField(max_length=100, null=True, blank=True) 
    text_note = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    state = models.CharField(max_length=3, choices= NOTE_STATUS , null=True, blank=True)

    id_comp = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pk)
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

STATUS_TACHE= {
    ('aff', 'A faire'),
    ('enc', 'En cours'),
    ('ter', 'Terminé'),
    ('enp', 'En pause'),
    ('ann', 'Annulé'),
}

PRIORITY = {
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
}

class Tache(models.Model):
    sommaire = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=3, choices=STATUS_TACHE, null=True, blank=True)
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    priorite = models.CharField(max_length=1, null=True, blank=True, choices=PRIORITY)

    assigner = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.DO_NOTHING)
    is_archived = models.BooleanField(default=False)

    id_comp = models.IntegerField(null=True, blank=True)

    num = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Tâche'
        verbose_name_plural='Tâches'

    def __str__(self):
        return self.sommaire
    
class Contact(models.Model):
    created_by = models.ForeignKey(User, on_delete= models.CASCADE)
    sujet = models.TextField(max_length=300, null=True, blank=True)
    messages = models.CharField(max_length=2000, null=True, blank=True)
    nom = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        verbose_name="Contact"
        verbose_name_plural="Contacts"

    def __str__(self):
        return self.created_by

DROITS = (
    ('lec', 'Lecture'),
    ('mod', 'Modification'),
    ('sup', 'Suppréssion'),
)

class DefineRights(models.Model):
    agent = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.CASCADE)
    rights = models.CharField(max_length=3, choices=DROITS, null=True, blank=True)

    class Meta:
        verbose_name="Droit d'accès"
        verbose_name_plural="Droits d'accès"

    def __str__(self):
        return self.agent  









    
