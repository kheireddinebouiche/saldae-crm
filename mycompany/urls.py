from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mycompany.views import *

app_name="mycompany"

urlpatterns = [
    
    path('configurer-mon-entreprise/', CreateMyCompany, name="configurer-mon-entreprise"),
    path('details-mon-entreprise/', ShowMyCompany, name="infos-mon-entreprise"),
    path('check-admin/', CheckForAdmin, name='check-for-admin' ),

]