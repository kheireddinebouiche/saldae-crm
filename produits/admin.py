from django.contrib import admin
from .models import *

admin.site.register(Typeproduit)
admin.site.register(Produit)
admin.site.register(Stock)
admin.site.register(MouvementStock)
