from re import T
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from leads.models import User

PLAN={ 
    ('free', 'Free'),
    ('basic', 'Basic'),
    ('pro', 'Pro.'),
}


class MyCompany(models.Model):
    designation = models.CharField(max_length=2000, null=True, blank=True)
    nif = models.CharField(max_length=100, null=True, blank=True)
    art = models.CharField(max_length=100, null=True, blank=True)
    nrc = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField()

    adresse1 = models.CharField(max_length=100, null=True, blank=True)
    nrue = models.CharField(max_length=5, null=True, blank=True)
    province = models.CharField(max_length=25, null=True, blank=True)
    etat = models.CharField(max_length=25, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    telephone = models.CharField(max_length=13, null=True, blank=True)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    fax = models.CharField(max_length=100, null=True, blank=True)

    niveau = models.CharField(max_length=10,choices=PLAN, null=True, blank=True)

    gestionnaire = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Mon entreprise"
        verbose_name_plural = "Mes entreprises"

    def __str__(self):
        return self.designation
