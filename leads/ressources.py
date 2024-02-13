from import_export import resources
from .models import *
from produits.models import *


class ClientResources(resources.ModelResource):
    class Meta:
        model = Client

class ProductResouces(resources.ModelResource):
    class Meta:
        model = Produit

class FournisseurResources(resources.ModelResource):
    class Meta:
        model = Fournisseurs