
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from leads.views import *

app_name="leads"

urlpatterns = [
    
    path('', home_page, name="home_page"),
    path('lead-list/', lead_list, name="lead_list"),
    path('<int:pk>/', lead_detail, name="lead_detail"),
    path('lead-create/', lead_create_view.as_view(), name="lead_create"),
    path('<int:pk>/update/', lead_update, name="lead_update"),
    path('<int:pk>/delete/', lead_delete, name="lead_delete"),
    path('Administration/',EnterToAdmin, name="Administration"),
    path('create-client/', CreateClient, name="create-client"),
    path('create-note/', CreateNote, name="create-note"),
    path('<int:pk>/update-note/', UpdateNote, name="update-note"),
    path('<int:pk>/delete-note/', DeleteNote, name="delete-note"),

    path('add-user-1/', RegisterAgent, name="add-user-1"),

    path('add-client/', AjouterClient, name="add-client"),
    path('list-dossier/', ListClient, name="list-dossier"),
    path('<int:pk>/update-client/', UpdateClient, name="update-client"),
    path('<int:pk>/delete-client/', DeleteClient, name="delete-client"),
    path('<int:pk>/details-client', detailsClient, name="details-client"),

    path('nouveau-devis/', NewDevis , name="nouveau-devis"),
    path('nouveau-devis-etape-2/',DevisEnCours, name="nouveau-devis-etape-2"),
    path('liste-des-devis/', ListDevis, name="liste-des-devis"),
    path('suppression-du-devis/<int:pk>/', SupprimerDevis, name="suppression-du-devis"),
    path('modification-du-devis/<int:pk>/',GetDevis, name="modification-du-devis"),
    path('AjouterAuDevis/<int:pk>/', AjouterAuDevis, name="AjouterAuDevis"),
    path('set-brouillon/<int:pk>/',ChangeStatBrouillon, name="set-brouillon"),
    path('sauvegarde-devis/<int:pk>/', ChangeStatSauvegrade, name="sauvegarde-devis"),

    path('list-utilisateurs/', ListUsers, name="list-utilisateur" ),
    path('<int:pk>/activate-user/', ActivateUser, name="activate-user"),
    path('<int:pk>/deactivate-user/', DeactivateUser, name="deactivate-user"),
    path('<int:pk>/update-user/', UpdateAgent, name="update-agent"),
    path('<int:pk>/delete-user/', DeleteUser, name="delete-user"),
    path('mon-profile/',my_profile, name="mon-profile"),

    path('ajouter-tache/', ajouter_tache, name="ajouter_tache"),
    path('list-taches/', list_taches, name="list-taches"),
    path('<int:pk>/details-tache/', details_tache, name="details-taches"),
    path('<int:pk>/modifier-tache/', modifier_tache, name="modifier-tache"),
    path('<int:pk>/supprimer-tache/', supprimer_tache, name="supprimer-tache"),
    path('<int:pk>/suppression-tache/', supprimer_tache_in_detail, name="suppression-tache"),
    path('<int:pk>/archiver-la-tache/', archive_tache, name="archiver-la-tache"),
    path('list-taches-archivees/', list_taches_archivees, name="list-taches-archivees"),
    path('<int:pk>/activer-la-tache/', activate_tache, name="activer-la-tache"),

    path('ajouter-fournisseur/', ajouter_fournisseur, name="ajouter-fournisseur"),
    path('<int:pk>/modifier-fournisseur/', modifier_fournisseur, name="modifier-fourniseur"),
    path('<int:pk>/details-fournisseur', details_fournisseur, name="details-fournisseurs"),
    path('<int:pk>/supprimer-fournisseur/', supprimer_fournisseur, name="supprimer-fournisseur"),
    path('liste-fournisseur/', liste_fournisseurs, name="liste-fournisseur"),

    ###### CLIENT IMPORT EXPORT ############################
    path('export-csv/', export_csv, name="export-csv"),
    path('export-xls/', export_xls, name="export-xls"),
    ###### END CLIENT IMPORT EXPORT ########################

    ###### PRODUCT IMPORT EXPORT ############################
    path('export-csv-produit/', export_csv_produit, name="export-csv-produit"),
    path('export-xls-produit/', export_xls_produit, name="export-xls-produit"),
    ###### END PRODUCT IMPORT EXPORT ########################


    path('Administration/contact/', affiche_contact, name="contact-us"),
    path('Administration/profile/mes-messages/', list_message, name="mes-messages"),
    

    ###### FORMULAIRES DE FILTRAGE ######################################################################
    path('resultat-de-recherche/', SearchClientView.as_view(), name='resultat-de-recherche'),
    path('resultat-recherche-devis/', FilterDevisView.as_view(), name="resultat-recherche-devis"),
    ###### FIN FORMULAIRES DE FILTRAGE ##################################################################

    ###### GESTION DES SECTEUR D ACTIVITE ###############################################################
    path('Administration/secteurs-activites/', index_secteur, name="index_secteur"),
    path('Administration/secteur-activitees/ajouter-secteur/', ajout_secteur, name="ajout_secteur"),
    path('Administration/secteur-activitess/supprimer-secteur/<int:pk>/', supprimer_secteur, name="supprimer-secteur"),
    path('Administration/secteur-activitess/modifier-secteur/<int:pk>/', modifier_secteur, name="modifier-secteur"),

    ###### FIN GESTION DES SECTEUR D ACTIVITE ###########################################################

]



