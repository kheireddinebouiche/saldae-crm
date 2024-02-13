
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
    path('plan-adhesion/', ViewPrincingListe, name="plan"),
    path('souscription-free/', freePlan, name="souscription-free" ),

    ########## GESTION DES NOTES ###################################################################
    path('Administration/traitement-note/', CreateNote, name="traitement-note"),
    path('Administration/<int:pk>/update-note/', UpdateNote, name="update-note"),
    path('Administration/<int:pk>/delete-note/', DeleteNote, name="delete-note"),
    path('Administration/cree-une-note/', NoteCreationView.as_view(), name='creer-une-not'),
    path('Administration/list-des-notes/', ListNote, name="liste-des-notes"),
    path('Administration/list-des-notes/<int:pk>/details-de-la-note',DetailsNote, name="details-de-la-note"),
    path('Administration/creer-une-note/', CheckCreateNote, name="create-note"),
    ########## FIN GESTION DES NOTES ###############################################################

    ########## GESTION DES AGENTS ##################################################################
    path('add-user-1/', RegisterAgent, name="add-user-1"),
    path('Administration/create-admin/', RegisterAgentAdmin, name="create-admin"),
    path('check-for-admin/', CheckForAdmin, name="check-for-admin"),
    path('Administration/mon-profile/mise-a-jour/', UpdateMyProfile, name="update-my-profile"),
    ########## FIN GESTION DES AGENTS ##############################################################

    ########## GESTION DES CLIENTS #################################################################
    path('Administration/ajouter-un-client/', AjouterClient, name="traitement-client"),
    path('Administration/add-client/',CheckCreateClient, name="add-client"),
    path('list-dossier/', ListClient, name="list-dossier"),
    path('<int:pk>/update-client/', UpdateClient, name="update-client"),
    path('<int:pk>/delete-client/', DeleteClient, name="delete-client"),
    path('<int:pk>/details-client', detailsClient, name="details-client"),
    path('recherche-par-secteur/', SearchClientViewBySecteur.as_view(), name="recherche-par-secteur"),
    ########## FIN GESTION DES CLIENTS #############################################################

    ########## GESTION DES DEVIS ###################################################################
    path('nouveau-devis/', NewDevis , name="nouveau-devis"),
    path('nouveau-devis-etape-2/',DevisEnCours, name="nouveau-devis-etape-2"),
    path('liste-des-devis/', ListDevis, name="liste-des-devis"),
    path('suppression-du-devis/<int:pk>/', SupprimerDevis, name="suppression-du-devis"),
    path('modification-du-devis/<int:pk>/',GetDevis, name="modification-du-devis"),
    path('AjouterAuDevis/<int:pk>/', AjouterAuDevis, name="AjouterAuDevis"),
    path('set-brouillon/<int:pk>/',ChangeStatBrouillon, name="set-brouillon"),
    path('sauvegarde-devis/<int:pk>/', ChangeStatSauvegrade, name="sauvegarde-devis"),
    ########### FIN GESTION DES DEVIS ##############################################################

    path('list-utilisateurs/', ListUsers, name="list-utilisateur" ),
    path('<int:pk>/activate-user/', ActivateUser, name="activate-user"),
    path('<int:pk>/deactivate-user/', DeactivateUser, name="deactivate-user"),
    path('<int:pk>/update-user/', UpdateAgent, name="update-agent"),
    path('<int:pk>/delete-user/', DeleteUser, name="delete-user"),
    path('mon-profile/',my_profile, name="mon-profile"),

    ######### GESTION DES TACHES ###################################################################
    path('ajouter-tache/', ajouter_tache, name="ajouter_tache"),
    path('list-taches/', list_taches, name="list-taches"),
    path('<int:pk>/details-tache/', details_tache, name="details-taches"),
    path('<int:pk>/modifier-tache/', modifier_tache, name="modifier-tache"),
    path('<int:pk>/supprimer-tache/', supprimer_tache, name="supprimer-tache"),
    path('<int:pk>/suppression-tache/', supprimer_tache_in_detail, name="suppression-tache"),
    path('<int:pk>/archiver-la-tache/', archive_tache, name="archiver-la-tache"),
    path('list-taches-archivees/', list_taches_archivees, name="list-taches-archivees"),
    path('<int:pk>/activer-la-tache/', activate_tache, name="activer-la-tache"),
    path('Administration/taches/taches-non-assigner/', ListTachNonAssigner , name="tache-non-assigner"),
    path('Administration/taches/taches-non-assigner/assigner-tache/<int:pk>/', AssignTache, name="assign-tache"),
    ########### FIN GESTION DES TACHES #############################################################

    ########### GESTION DES FOURNISSEURS ###########################################################
    path('Administration/ajouter-un-fournisseur/', ajouter_fournisseur, name="ajouter-fournisseur"),
    path('Administration/<int:pk>/modifier-un-fournisseur/', modifier_fournisseur, name="modifier-fourniseur"),
    path('Administration/<int:pk>/details-un-fournisseur', details_fournisseur, name="details-fournisseurs"),
    path('Administration/<int:pk>/supprimer-un-fournisseur/', supprimer_fournisseur, name="supprimer-fournisseur"),
    path('Administration/liste-des-fournisseurs/', liste_fournisseurs, name="liste-fournisseur"),
    ########## FIN GESTION DES FOURNISSEURS #######################################################

    ###### CLIENT IMPORT EXPORT ###################################################################
    path('export-csv/', export_csv, name="export-csv"),
    path('export-xls/', export_xls, name="export-xls"),
    ###### END CLIENT IMPORT EXPORT ###############################################################

    ###### FOURNISSEUR IMPORT EXPORT ###################################################################
    path('export-csv-fournisseur/', export_csv_fournisseur, name="export-csv-fournisseur"),
    path('export-xls-fournisseur/', export_xls_fournisseur, name="export-xls-fournisseur"),
    ###### END FOURNISSEUR IMPORT EXPORT ###############################################################


    ###### PRODUCT IMPORT EXPORT ##################################################################
    path('export-csv-produit/', export_csv_produit, name="export-csv-produit"),
    path('export-xls-produit/', export_xls_produit, name="export-xls-produit"),
    ###### END PRODUCT IMPORT EXPORT ##############################################################


    path('Administration/contact/', affiche_contact, name="contact-us"),
    path('Administration/profile/mes-messages/', list_message, name="mes-messages"),
    

    ###### FORMULAIRES DE FILTRAGE ######################################################################
    path('resultat-de-recherche/', SearchClientView.as_view(), name='resultat-de-recherche'),
    path('resultat-recherche-devis/', FilterDevisView.as_view(), name="resultat-recherche-devis"),
    path('resultat-recherche-fournisseurs/', SearchFournisseurView.as_view(), name='recherche-fournisseurs'),
    path('resultat-recherche-rendez-vous/', FilterRdv.as_view(), name="recherche-rdv"),
    ###### FIN FORMULAIRES DE FILTRAGE ##################################################################

    ###### GESTION DES SECTEUR D ACTIVITE ###############################################################
    path('Administration/secteurs-activites/', index_secteur, name="index_secteur"),
    path('Administration/secteur-activitees/ajouter-secteur/', ajout_secteur, name="ajout_secteur"),
    path('Administration/secteur-activitess/supprimer-secteur/<int:pk>/', supprimer_secteur, name="supprimer-secteur"),
    path('Administration/secteur-activitess/modifier-secteur/<int:pk>/', modifier_secteur, name="modifier-secteur"),
    ###### FIN GESTION DES SECTEUR D ACTIVITE ###########################################################

    ###### DEBUT HELP ###################################################################################
    path('Administration/get-help/', IndexHelp, name="index-help"),
    path('Administration/modification-faq/<int:pk>/', AlterFaq, name='modification-faq'),
    path('Administration/supprimer-faq/<int:pk>/', SuppFaq, name="supprimer-faq"),
    path('Administration/posez-une-question/', AskQuestion, name="poser-une-question"),
    path('Administration/ma-liste-de-question/', MesQuestion, name="ma-liste-de-question"),
    ###### FIN HELP #####################################################################################

    #########  NOT FOUND AND ERROR NOT FOUND ############################################################
    path('404-not-found/', NotFound, name="not-found"),
    path('erreur/', Error, name='erreur'),
    ######### FIN NOT FOUND AND ERROR NOT FOUND #########################################################

    ######### GESTION DES RENDEZ VOUS ###################################################################
    path('Administration/list-rendez-vous/', ListRdv, name="list-rendez-vous"),
    path('Administration/list-rendez-vous/ajouter-un-rendez-vous/', AjoutRdv, name="ajouter-rendez-vous"),
    path('Administration/list-rendez-vous/<int:pk>/details-rendez-vous/', DetailsRdv, name="details-rendez-vous"),
    path('Administration/list-rendez-vous/<int:pk>/supprimer-rendez-vous/', RemoveRdv, name="supp-rendez-vous"),
    path('Administration/list-rendez-vous/<int:pk>/mise-a-jour-rendez-vous/', UpdateRdv, name="miseajour-rendez-vous"),
    ######### FIN GESTION DES RENDEZ VOUS ###############################################################
]



