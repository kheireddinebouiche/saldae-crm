from asyncio.windows_events import NULL
from django.shortcuts import render, redirect, reverse
from .models import Agent, Lead, Note
from django.http import HttpResponse, response
from .forms import *
from django.db import transaction
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django.http import HttpResponse
from .ressources import *
from django.contrib import messages
from django.views.generic import ListView

from django.db.models import Q
from help.models import *
from mycompany.models import *
from mycompany.views import *
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy


####### IMPORT EXPORT VIEW CLIENT ###################################################
def export_xls(request):
    client_resource = ClientResources()
    dataset = client_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ListeClients.xls"'
    return response
def export_csv(request):
    client_resource = ClientResources()
    dataset = client_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ListeClients.csv"'
    return response
####### END IMPORT EXPORT VIEW CLIENT ###############################################

####### IMPORT EXPORT VIEW FOURNISSEUR ###################################################
def export_xls_fournisseur(request):
    fournisseur_resource = FournisseurResources()
    dataset = fournisseur_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ListeFournisseur.xls"'
    return response
def export_csv_fournisseur(request):
    fournisseur_resource = FournisseurResources()
    dataset = fournisseur_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ListeFournisseur.csv"'
    return response
####### END IMPORT EXPORT VIEW FOURNISSEUR ###############################################

###### IMPORT EXPORT VIEW PRODUCT ###################################################
def export_xls_produit(request):
    product_resource = ProductResouces()
    dataset = product_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ListeProduits.xls"'
    return response
def export_csv_produit(request):
    product_resource = ProductResouces()
    dataset = product_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ListProduits.csv"'
    return response
###### END EXPORT VIEW PRODUCT ######################################################

############ GESTION DES LISTE DE PRIX ##############################################
def  ViewPrincingListe(request):
    return render(request, 'pricing-plan.html')
############ FIN GESTION DES LISTE DE PRIX ##########################################

@login_required(login_url='/login/')
def EnterToAdmin(request):
    if request.user.is_authenticated:
        if request.user.agent.user_type == 'ad' or request.user.is_staff:
            note = Note.objects.filter(created_by=request.user)
            client = Client.objects.all().count()
            fournisseur = Fournisseurs.objects.all().count()
            produit = Produit.objects.all().count()
            agent = User.objects.all().count()
            company = MyCompany.objects.all()

            context = {
                'note' : note,
                'client': client,
                'fournisseur' : fournisseur,
                'produit' : produit,
                'agent' : agent,
                'company' : company,
            }
            return render(request, 'Administration/index.html',context)
        else:
            return HttpResponse("Vous n'étes pas autoriser à accèder à cette partie du site")
    else:
        return redirect('login')

@login_required(login_url='/login/')
@transaction.atomic
def CreateClient(request):
    if request.user.Agent.user_type == 'ad':
        return render(request, 'Administration/create_client.html')
    else:
        return HttpResponse("Vous n'étes pas autoriser à accèder à cette partie du site")

@transaction.atomic
@login_required(login_url='/login/')
def RegisterVenderUser(request):
    if request.method == 'POST':
        form = CustomAgentCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.agent.num_identification = form.cleaned_data.get('num_identification')
            user.agent.user_type='ag'
            user.save()
            redirect('login')
    else:

        form = CustomAgentCreationForm()
        context = {
            'form' : form,
        }
        return render(request,'Administration/Create-user-vender.html', context)

@transaction.atomic
@login_required(login_url='/login/')
def RegisterAgent(request):
    if request.user.agent.user_type == 'ad':
        if request.method == 'POST':
            form = CustomAgentCreationForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()
                user.agent.num_identification = form.cleaned_data.get('num_identification')
                user.agent.user_type = form.cleaned_data.get('user_type')  
                user.agent.image = form.cleaned_data.get('image')
                user.agent.id_company = request.user.agent.id_company
                user.save()
                return redirect('leads:list-utilisateur')
            else:
                return HttpResponse("Erreur lors du traitement des données.")
        else:
            form = CustomAgentCreationForm()
            context = {
                'form' : form,
            }
            return render(request,'Administration/ajouter-utilisateur.html', context)
    else:

        return redirect("leads:erreur")
   
class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

def landing_page(request):
    return render(request, 'front/index.html')
    
def home_page(request):
    
    return redirect('landing_page')

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads' : leads
    }

    return render(request, "leads/lead_list.html", context)

def lead_detail(request, pk):

    lead = Lead.objects.get(id=pk)

    context = {
        'lead' : lead,
    }
    
    return render(request, 'leads/lead_detail.html', context)

class lead_create_view(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')

    def form_valid(self, form):
        #todo send email
        send_mail(
            subject = "Un nouveau prospect à été créer",
            message = "Entrer dans la plateforme pour consulter les détails",
            from_email = "test@test.com",
            recipient_list = ['test2@test.com'],
        )
        return super(lead_create_view, self).form_valid(form)

def lead_update(request, pk):

    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance = lead)
    
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance = lead)
        if form.is_valid():
            form.save()
            return redirect('leads:lead_list')

    context = {
        'lead' : lead,
        'form' : form,
    }

    return render(request, 'leads/lead_update.html', context)

def lead_delete(request, pk):

    lead = Lead.objects.get(id=pk)

    lead.delete()

    return redirect('leads:lead_list')

##### Gestion des notes#########################################################################################

def CheckCreateNote(request):
    try:
        element = Note.objects.filter(id_comp = request.user.agent.id_company)
        if element.count() == 4:
            return HttpResponse('Vous avez atteint la limite de création des notes, veuillez mettre à jour votre plan. ')
        else:
            return redirect('leads:traitement-note')
    except:
        return redirect('leads:traitement-note')

@login_required(login_url='/login/')
@transaction.atomic
def CreateNote(request):

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():

            try:
                number = Note.objects.filter(id_comp = request.user.agent.id_company).last()
                n= number.num + 1
            except:
                n=1
         
            titre = form.cleaned_data.get('titre')
            text_note = form.cleaned_data.get('text_note')           
            note = Note(
                created_by = request.user,
                titre = titre,
                text_note =  text_note,
                id_comp = request.user.agent.id_company,
                num = n
            )
            note.save()
            return redirect('leads:liste-des-notes')
        else:
            return HttpResponse("Une erreur c'est produite durant le traitement de vos données")
    else:
        form = NoteForm()
        context = {
            'form' : form
        }
        return render(request, 'Administration/create_new_note.html', context)

@login_required(login_url='/login/')
@transaction.atomic
def UpdateNote(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance = note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance = note)
        if form.is_valid():
            form.save()
            return redirect('leads:Administration')
    else:
        context = {
            'note': note,
            'form' : form,
        }
        return render(request, 'Administration/note_modification.html', context)

@login_required(login_url='/login/')
def DeleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('leads:Administration')

@login_required(login_url='/login/')
def ListNote(request):
    id_comp = MyCompany.objects.get(id = request.user.agent.id_company)
    note = Note.objects.filter(id_comp = id_comp.id)
    context = {
        'note' : note,
    }
    return render(request, 'Administration/list-des-notes.html', context)

class NoteCreationView(BSModalCreateView):
    template_name = 'Administration/modal-create-note.html'
    form_class = BookModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('leads:Administration')

@login_required(login_url='/login/')
def DetailsNote(request, pk):
    note = Note.objects.get(id=pk)
    context = {
        'note' : note,
    }
    return render(request, 'Administration/details-de-la-note.html', context)
###### Fin gestion des notes ###################################################################################

######### GESTION DES AGENT / UTILISATEURS #####################################################################
@login_required(login_url='/login/')
def ActivateUser(request ,pk):
    agent = User.objects.get(id=pk)
    agent.is_active=True
    agent.save()

    return redirect('leads:list-utilisateur')

@login_required(login_url='/login/')
def DeactivateUser(request, pk):
    agent = User.objects.get(id=pk)
    agent.is_active = False
    agent.save()

    return redirect('leads:list-utilisateur')

@login_required(login_url='/login/')
def DeleteUser(request, pk):
    agent = User.objects.get(id=pk)
    agent.delete()
    return redirect('leads:list-utilisateur')

@login_required(login_url='/login/')
def ListUsers(request):
  
    id_comp = MyCompany.objects.get(id = request.user.agent.id_company)
    agents = Agent.objects.filter(id_company=id_comp.id)
    context = {
        'agents': agents,
    }
    return render(request, 'Administration/list-utilisateurs.html', context)

@login_required(login_url='/login/')
def UpdateAgent(request, pk):
    agent = User.objects.get(id=pk)
    profile = Agent.objects.get(user=agent)

    form1 = AgentForm(instance=agent)
    form2 = AgentProfile(instance=profile)
    
    if request.method == 'POST':
        form1 = AgentForm(request.POST, instance=agent)
        form2 = AgentProfile(request.POST,request.FILES, instance=profile)
        if form1.is_valid() and form2.is_valid():   
            form1.save()
            form2.save()
            return redirect('leads:update-agent', pk= agent.id)

    context = {
        'agent' : agent,
        'form1' : form1,
        'form2' : form2,
    }

    return render(request, 'Administration/update-user.html', context)

@login_required(login_url='/login/')
def my_profile(request):
    agent = Agent.objects.get(user = request.user)

    context= {
        'agent' : agent, 
    }

    return render(request, 'Administration/agent-profile.html', context)

@login_required(login_url='/login/')
@transaction.atomic
def UpdateMyProfile(request):
    profile = Agent.objects.get(user = request.user)
    form1 = AgentUpdateProfile(instance=profile) 
    form2 = AgentForm(instance=request.user)

    if request.method == "POST":
        form1 = AgentUpdateProfile(request.POST, request.FILES, instance=profile)
        form2 = AgentForm(request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(request, "Vos information ont été mis à jour.")
            return redirect('leads:Administration')
        else:
            messages.error(request, "Une erreure est survenu lors du traitement de l'information.")
            return HttpResponse('Une erreur est survenue lors du traitement de l\'information.')
            
    else:

        context = {
            'form1' : form1,
            'form2' : form2,
        }

        return render(request,"Administration/update-my-profile.html", context)

@transaction.atomic
def RegisterAgentAdmin(request):
    if request.method == 'POST':
        form = CustomAgentAdmin(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.agent.num_identification = form.cleaned_data.get('num_identification')
            user.agent.user_type = form.cleaned_data.get('user_type')  
            user.agent.image = form.cleaned_data.get('image')
            user.agent.user_type = 'ad'
            user.is_staff = True
            user.save()
            messages.success(request,'Bienvenue dans votre tableau de bord.')
            return redirect('leads:administration')
        else:
            return HttpResponse("Erreur lors du traitement des données.")

    else:

        form = CustomAgentAdmin()
        context = {
            'form' : form,
        }
        return render(request,'Administration/creation-dun-admin.html', context)
######## FIN GESTION DES UTILISATEURS / AGENT ##################################################################

###### GESTION DES CLIENTS #############################################################################
@login_required(login_url='/login/')
def ListClient(request):

    if request.user.agent.user_type == 'ad':
        id_comp = MyCompany.objects.get(id = request.user.agent.id_company)
        client = Client.objects.filter(id_comp = id_comp.id)
        context = {
            'client' : client,
        }

        return render(request, 'Administration/liste-dossier-client.html', context)
    else:

        client = Client.objects.filter(created_by = request.user)

        context = {
            'client' : client
        }

        return render(request, 'Administration/liste-dossier-client.html', context)

@login_required(login_url='/login/')
def CheckCreateClient(request):
    try:
        number = Client.objects.filter(id_comp = request.user.agent.id_company)
        if number.count() == 2:
            return HttpResponse("Vous avez atteint le maximum de création de compte client, veuillez changer de plan.")
        else:
            return redirect('leads:traitement-client')
    except:
        return redirect('leads:traitement-client')

@login_required(login_url='/login/')
def AjouterClient(request):
     
        if request.method == 'POST':

            form = ClientForm(request.POST)
            try:
                number = Client.objects.filter(id_comp = request.user.agent.id_company).last()
                n= number.num + 1
            except:
                n=1

            if form.is_valid():
                raison = form.cleaned_data.get('raison')
                adresse = form.cleaned_data.get('adresse')
                gerant = form.cleaned_data.get('gerant')
                telephone = form.cleaned_data.get('telephone')
                rue = form.cleaned_data.get('rue') 
                province = form.cleaned_data.get('province')
                pays = form.cleaned_data.get('pays')
                zip = form.cleaned_data.get('zip')
                categorie_client = form.cleaned_data.get('categorie_client')
                fax = form.cleaned_data.get('fax')
                email = form.cleaned_data.get('email')
                secteur = form.cleaned_data.get('secteur')
                nrc = form.cleaned_data.get('nrc')
                nif = form.cleaned_data.get('nif')
                art = form.cleaned_data.get('art')

                client = Client (
                    raison = raison,
                    adresse = adresse,
                    gerant = gerant,
                    telephone = telephone,
                    rue = rue,
                    province = province,
                    pays = pays,
                    zip = zip,
                    categorie_client = categorie_client,
                    fax = fax,
                    email = email,
                    created_by = request.user,
                    secteur = secteur,
                    nrc = nrc,
                    nif = nif,
                    art = art,
                    num = n,
                    id_comp = request.user.agent.id_company
                )

                client.save()
                messages.success(request,'Le dossier client à été créer avec succèes !')
                return redirect('leads:list-dossier')
            else:
                return HttpResponse("Une erreur c'est produite lors du traitement de vos données.")
        else:

            form = ClientForm()
            context = {
                'form' : form,
            }

            return render(request, 'Administration/add-client.html', context)

@login_required(login_url='/login/')
def UpdateClient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance = client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance = client)
        if form.is_valid():
            form.save()
            return redirect('leads:Administration')

        else:
            return HttpResponse("Une erreure c'est produite lors du traitement de vos données.")
    else:

        context = {
            'client' : client,
            'form' : form,
        }

        return render(request, 'Administration/update-client.html', context)

@login_required(login_url='/login/')
def DeleteClient(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    return redirect('leads:Administration')

@login_required(login_url='/login/')
def detailsClient(request, pk):
    client = Client.objects.get(id = pk)
    rdv = RendezVous.objects.all().filter(client__id = client.id)
    tache = Tache.objects.all().filter(client__id = client.id)
    context = {
        'client' : client,
        'rdv' : rdv,
        'tache' : tache,
    }
    return render(request, 'Administration/details-client.html', context)
###### Fin gestion des clients #################################################################################

############# GESTION DES  DEVIS #####################################################################################
@login_required(login_url='/login/')
@transaction.atomic
def NewDevis(request):
    form = DevisForm()
    if request.method == 'POST':
        form = DevisForm(request.POST)

        try:
            n = Devis.objects.all().filter(id_comp = request.user.agent.id_company)
            n = n + 1 
        except:
            n = 1

        if form.is_valid():
            prospet = form.cleaned_data.get('prospet')
            status = form.cleaned_data.get('status')
            date_du_bon = form.cleaned_data.get('date_du_bon')
            observation = form.cleaned_data.get('observation')
            adresse_livraison = form.cleaned_data.get('adresse_livraison')
            methode_paiement = form.cleaned_data.get('methode_paiement')

            devis = Devis(
                user = request.user,
                prospet = prospet,
                status = status,
                date_du_bon = date_du_bon,
                observation = observation,
                adresse_livraison = adresse_livraison,
                methode_paiement = methode_paiement,
                etat = 'enc',
                id_comp = request.user.agent.id_company,
                num = n,
            )

            devis.save()
            messages.success(request, 'Le devis à été créer avec succées, passer a la seconde étape')
            return redirect('leads:nouveau-devis-etape-2')
        else:
            messages.error(request, "Une erreur est survenu lors de la validation des données, veuillez contacter l'administrateur.")
            return redirect('leads:nouveau-devis')
    else:

        context = {
            'form' : form,
        }    
        return render(request, 'Administration/nouveau-devis-etape-1.html', context)

@login_required(login_url='/login/')
def DevisEnCours(request):
    devis = Devis.objects.get(user=request.user, etat='enc')
    form = ProduitsDevisForm()

    if request.method == 'POST':
        form = ProduitsDevisForm(request.POST)
        if form.is_valid():
                produit = form.cleaned_data.get('product')
                prix = form.cleaned_data.get('prix')
                qtr = form.cleaned_data.get('qtr')
                remise = form.cleaned_data.get('remise')

                ligne_devis = ProduitsDevis(
                    product = produit,
                    qtr = qtr,
                    prix = prix,
                    remise = remise,
                    total = qtr * prix,
                )

                ligne_devis.save()
                devis.lignes_devis.add(ligne_devis)
               
                messages.success(request,'Le produit a été bien ajouter.')
                return redirect('leads:nouveau-devis-etape-2')
        else:
            messages.error(request, "Une erreur c'est produite lors du traitement de la requête.")
            return redirect('leads:nouveau-devis-etape-2')

    context = {
        'devis' : devis,
        'form' : form,
    }

    return render(request, 'Administration/nouveau-devis-etape-2.html', context)

@login_required(login_url='/login/')
def ListDevis(request):
    devis = Devis.objects.all().filter(id_comp = request.user.agent.id_company)
    form = DropDownDevisState()

    context = {
        'devis' : devis,
        'form' : form, 
    }

    return render(request, 'Administration/liste-des-devis.html', context)

@login_required(login_url='/login/')
def SupprimerDevis(request, pk):
    devis = Devis.objects.get(id = pk)
    devis.delete()
    messages.success(request,'Le devis à été supprimer avec succès.')
    return redirect('leads:liste-des-devis')

@login_required(login_url='/login/')
def GetDevis(request, pk):
    devis = Devis.objects.get(id = pk)

    if devis.etat == 'enc' or devis.etat == 'bro' or devis.etat == 'sau':
        form = ProduitsDevisForm()
        if request.method == 'POST':
            form = ProduitsDevisForm(request.POST)
            if form.is_valid():
                produit = form.cleaned_data.get('product')
                prix = form.cleaned_data.get('prix')
                qtr = form.cleaned_data.get('qtr')
                remise = form.cleaned_data.get('remise')

                ligne_devis = ProduitsDevis(
                    product = produit,
                    qtr = qtr,
                    prix = prix,
                    remise = remise,
                    total = qtr * produit.prix,
                )

                ligne_devis.save()
                devis.lignes_devis.add(ligne_devis)
               
                messages.success(request,'Le produit a été bien ajouter.')
                return redirect('leads:modification-du-devis' , pk = devis.id)
            else:

                messages.error(request, "Une erreur c'est produite lors du traitement de la requête.")
                return redirect('leads:modification-du-devis', pk=devis.id)
        else:
            context = {
                'form' : form,
                'devis' : devis,
            }
            return render(request, 'Administration/nouveau-devis-etape-2.html', context)

@login_required(login_url='/login/')
def AjouterAuDevis(request, pk):
        devis = Devis.objects.filter(id = pk)
        form = ProduitsDevisForm()
        if request.method == "POST":
            form = ProduitsDevisForm(request.POST)
            if form.is_valid():
                produit = form.cleaned_data.get('product')
                prix = form.cleaned_data.get('prix')
                qtr = form.cleaned_data.get('qtr')
                remise = form.cleaned_data.get('remise')

                ligne_devis = ProduitsDevis(
                    product = produit,
                    qtr = qtr,
                    prix = prix,
                    remise = remise,
                    total = qtr * prix,
                )

                d = devis.lignes_devis.add(ligne_devis)
                d.save()

                messages.success(request,'Le produit a été bien ajouter.')
                return redirect('leads:GetDevis')

@login_required(login_url='/login/')
def ChangeStatBrouillon(request, pk):
    devis = Devis.objects.get(id =pk)
    devis.etat = 'bro'
    devis.save()
    messages.success(request,'Brouillon enregistrer avec succèes.')
    return redirect('leads:liste-des-devis')

@login_required(login_url='/login/')
def ChangeStatSauvegrade(request, pk):
    devis = Devis.objects.get(id = pk)

    if devis.lignes_devis.count == 0:
        messages.info(request,"Veuillez ajouter des produits/articles avant de sauvegarder !")
        return redirect('leads:nouveau-devis-etape-2')
    else:
        devis.etat = 'sau'
        devis.save()
        messages.success(request, 'Devis sauvegrader avec succès.')
        return redirect('leads:liste-des-devis')
############# FIN DE GESTION DEVIS ############################################################################

############## GESTION DES TACHES #############################################################################
@login_required(login_url='/login/')
@transaction.atomic
def ajouter_tache(request):
    form = TachesForm(user = request.user.agent.id_company)
    if request.method == 'POST':
        form = TachesForm(request.user.agent.id_company, request.POST)
        
        try:            
            number = Tache.objects.filter(id_comp = request.user.agent.id_company).last()
            n= number.num + 1
        except:
            n=1

        if form.is_valid():
            sommaire = form.cleaned_data.get('sommaire')
            description = form.cleaned_data.get('description')
            date_debut = form.cleaned_data.get('date_debut')
            date_fin = form.cleaned_data.get('date_fin')
            status = form.cleaned_data.get('status')
            client = form.cleaned_data.get('client')
            priorite = form.cleaned_data.get('priorite')
            assigner = form.cleaned_data.get('assigner')

            tache = Tache(
                sommaire = sommaire,
                description = description,
                date_debut = date_debut,
                date_fin = date_fin, 
                status = status,
                client = client,
                assigner = assigner,
                priorite = priorite,
                num = n,
                id_comp = request.user.agent.id_company,
            )

            tache.save()
            return redirect('leads:list-taches')
        
    context = {
        'form': form,
    }
    return render(request, 'Administration/ajouter_tache.html', context)

@login_required(login_url='/login/')
def modifier_tache(request, pk):
    tache = Tache.objects.get(id=pk)
    form = TachesForm(instance=tache)
    if request.method == 'POST':
        form = TachesForm(request.POST, instance=tache)
        if form.is_valid():  
            form.save()
            return redirect('leads:modifier-tache', pk=tache.id)
               
    context = {
        'tache' : tache,
        'form' : form,
    }
    return render(request, 'Administration/modifier_tache.html', context)

@login_required(login_url='/login/')
def supprimer_tache(request, pk):
    tache = Tache.objects.get(id=pk)
    tache.delete()
    return redirect('leads:list-taches')

@login_required(login_url='/login/')
def details_tache(request, pk):
    tache = Tache.objects.get(id=pk)
    context = {
        'tache' : tache,
    }

    return render(request, 'Administration/details_tache.html', context)

@login_required(login_url='/login/')
def list_taches(request):
    taches = Tache.objects.filter(is_archived=False, id_comp = request.user.agent.id_company)
    
    tache_a_faire = Tache.objects.filter(status = 'aff')
    tache_annuler = Tache.objects.filter(status = 'ann')
    tache_en_cour = Tache.objects.filter(status = 'enc')
    tache_non_ass = Tache.objects.filter(assigner__isnull = True)

    context = {
        'taches' : taches,
        'tache_a_faire' : tache_a_faire,
        'tache_annuler' : tache_annuler,
        'tache_en_cour' : tache_en_cour,
        'tache_non_ass' : tache_non_ass,
    }

    return render(request, 'Administration/liste_taches.html', context)

@login_required(login_url='/login/')
def supprimer_tache_in_detail(request, pk):
    tache = Tache.objects.get(id=pk)
    tache.delete()

    return redirect('leads:details-tache', pk=tache.id)

@login_required(login_url='/login/')
def archive_tache(request, pk):
    tache = Tache.objects.get(id=pk)
    tache.is_archived = True
    tache.save()
    return redirect('leads:list-taches')

@login_required(login_url='/login/')
def activate_tache(request, pk):
    tache = Tache.objects.get(id=pk)
    tache.is_archived=False
    tache.save()
    return redirect('leads:list-taches-archivees')

@login_required(login_url='/login/')
def list_taches_archivees(request):
    taches = Tache.objects.filter(is_archived=True, id_comp = request.user.agent.id_comp)
    context = {
        'taches' : taches,
    }

    return render(request, 'Administration/list-taches-archivees.html', context)

@login_required(login_url='/login/')
def ListTachNonAssigner(request):
    if request.user.agent.user_type == "ad":

        taches = Tache.objects.filter(id_comp = request.user.agent.id_company, assigner__isnull = True)

        context = {
            'taches' : taches,
        }

        return render(request, 'Administration/taches-non-assigner.html', context)
    else:

        return redirect('leads:erreur')

@login_required(login_url='/login/')
def AssignTache(request, pk):
    tache = Tache.objects.get(id=pk)
    form = AssignTachForm(user = request.user.agent.id_company,instance=tache)

    context = {
        'form' : form
    }

    return render(request, 'Administration/assign-tache.html', context)

################ FIN GESTION DES TACHES########################


################ GESTION DES FOURNISSEURS #####################
@login_required(login_url='/login/')
@transaction.atomic
def ajouter_fournisseur(request):
    if request.user.agent.user_type == "ad":
        form = FournisseursForm()
        if request.method == 'POST':
            form = FournisseursForm(request.POST, request.FILES)
            
            try:
                number = Fournisseurs.objects.filter(id_comp = request.user.agent.id_company).last()
                n= number.num + 1
            except:
                n=1

            if form.is_valid():
                raison = form.cleaned_data.get('raison')
                adresse = form.cleaned_data.get('adresse')
                mobile = form.cleaned_data.get('mobile')
                image = form.cleaned_data.get('image')
                telephone = form.cleaned_data.get('telephone')
                email= form.cleaned_data.get('email')
                fournisseur_type= form.cleaned_data.get('fournisseur_type')
                nis= form.cleaned_data.get('nis')
                nif= form.cleaned_data.get('nif')
                art= form.cleaned_data.get('art')
                pays = form.cleaned_data.get('pays')
                secteur = form.cleaned_data.get('secteur')
                province = form.cleaned_data.get('province')

                fournisseurs = Fournisseurs(

                    raison = raison,
                    adresse= adresse,
                    mobile= mobile,
                    image = image,
                    telephone= telephone,
                    email= email,
                    fournisseur_type= fournisseur_type,
                    nis= nis,
                    nif= nif,
                    art= art,
                    pays = pays,
                    secteur = secteur,
                    provine = province,
                    num = n,
                    id_comp = request.user.agent.id_company,
                )

                fournisseurs.save()
                return redirect('leads:liste-fournisseur')

            else: 
                return HttpResponse('Une erreur est survenu lors du traitement des données, veuillez contacter l\'administrateur.')
        context = {
            'form' : form,
        }
        return render(request, 'Administration/ajouter-fournisseur.html',context)
    else:
        return redirect('leads:erreur')

@login_required(login_url='/login/')
def details_fournisseur(request, pk):
    fournisseur = Fournisseurs.objects.get(id = pk)
    context = {
        'fournisseur' : fournisseur
    }
    return render(request, 'Administration/details-fournisseur.html', context)

@login_required(login_url='/login/')
def modifier_fournisseur(request, pk):
    fournisseur = Fournisseurs.objects.get(id = pk)
    form = FournisseursForm(instance=fournisseur)
    if request.method == 'POST':
        form = FournisseursForm(request.POST,request.FILES, instance=fournisseur)
        if form.is_valid:
            form.save()
            return redirect('leads:modifier-fournisseur', pk=fournisseur.id)
    context = {
        'fournisseur': fournisseur,
        'form' : form,
    }
    return render(request, 'Administration/modifier-fournisseur.html', context)

@login_required(login_url='/login/')
def supprimer_fournisseur(request, pk):
    fournisseur = Fournisseurs.objects.get(id=pk)
    fournisseur.delete()
    return redirect('leads:liste-fournisseur')

@login_required(login_url='/login/')
def liste_fournisseurs(request):
    fournisseurs = Fournisseurs.objects.all().filter(id_comp = request.user.agent.id_company)
    context = {
        'fournisseurs' : fournisseurs,
    }
    return render(request, 'Administration/liste-fournisseur.html', context)
################ FIN GESTION DES FOURNISSEURS #################


############### GESTION DU CALENDRIER #########################

################ FIN GESTION DU CALENDRIER ####################

################ GESTION DE LA PAGE SUPPORT / CONTACT #########
def affiche_contact(request):
    form = ContactForm()

    context = {
        'form' : form,
    }
    return render(request, 'Administration/contact.html',context)

def list_message(request):
    contact = Contact.objects.filter(created_by = request.user)

    context = {
        'contact' : contact,
    }

    return render(request, 'Administration/liste-contact.html', context)

################# FIN GESTION DE LA PAGE SUPPORT / CONTACT ####

################# DEBUT FILTRES ET RECHERCHES ######################
class SearchClientView(ListView):
    model = Client
    template_name='Administration/recherches/resultats-de-recherche.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Client.objects.filter(
            Q(raison__icontains=query)
        )
        return object_list

class SearchFournisseurView(ListView):
    model = Fournisseurs
    template_name='Administration/recherches/resultats-de-recherche-fournisseurs.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Fournisseurs.objects.filter(
            Q(raison__icontains=query)
        )
        return object_list

class FilterDevisView(ListView):
    model = Devis
    template_name='Administration/resultats/resultats-de-recherche-devis.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Devis.objects.filter(
            Q(prospet = query)
        )
        return object_list

class FilterRdv(ListView):
    model = RendezVous
    template_name='Administration/resultats-de-recherche-rdv.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = RendezVous.objects.filter(
            Q(client = query)
        )
        return object_list

################ FIN FILTRES ET RECHERHCES ##########################

########## GESTION DES IMPRESSION PDF ###############################

########## FIN GESTION DES IMPRESSION PDF ###########################

########## GESTION DES SECTEURS D ACTIVITEES ##################
def index_secteur(request):
    libelle = SecteurActivite.objects.all()
    
    context = {
        'libelle' : libelle,
    }

    return render(request,'Administration/ajout_secteur_activite.html', context)

def ajout_secteur(request):
    form = SecteurActiviteForm()
    if request.method == 'POST':
        form = SecteurActiviteForm(request.POST)
        if form.is_valid():
            libelle = form.cleaned_data.get('libelle')

            secteur = SecteurActivite(
                libelle = libelle,
            )

            secteur.save()
            messages.success(request,"Enregistrement avec succées.")
            return redirect("leads:index_secteur")

        else:
            messages.error(request,"Une erreur c'est produite lors du traitement de la requête.")
            return redirect('leads:index_secteur')

    context = {
        'form' : form,
    }

    return render(request,'Administration/formulaire_ajout_secteur.html', context)

def supprimer_secteur(request, pk):
    secteur = SecteurActivite.objects.get(id=pk)
    secteur.delete()
    messages.success(request,"Le secteur d'activité à été supprimer.")
    return redirect("leads:index_secteur")

def modifier_secteur(request, pk):
    secteur = SecteurActivite.objects.get(id=pk)
    form = SecteurActiviteForm(instance=secteur)
    if request.method == 'POST':
        form = SecteurActiviteForm(request.POST, instance=secteur)
        form.save()
        messages.success(request, "Modificiation effectuer avec succès.")
        return redirect('leads:index_secteur')

    context = {
        'form': form,
        'secteur' : secteur,
    }

    return render(request, 'Administration/formulaire_modification_secteur.html', context)

class SearchClientViewBySecteur(ListView):
    model = Client
    template_name='Administration/resultats-de-recherche.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Client.objects.filter(
            Q(secteur__icontains=query)
        )
        return object_list
########## FIN GESTION DES ACTIVITEES #########################

########## DEBUT HELP #########################################
@login_required(login_url='/login/')
def IndexHelp(request):
    return render(request, "Administration/help.html")

@login_required(login_url='/login/')
def GetHelp(request):
    return render(request,'Administration/get-help.html')

@login_required(login_url='/login/')
@transaction.atomic
def AddQuestionFAQ(request):
    return render(request, 'Administration/formulaire-ajout-question.html')

@login_required(login_url='/login/')
def SuppFaq(request, pk):
    faq = Faq.objects.get(id=pk) 
    faq.delete()
    messages.success(request, "La faq à été supprimer.")
    return redirect('leads:index-leads') 

@login_required(login_url='/login/')
def AlterFaq(request, pk):
    faq = Faq.objects.get(id=pk)
    form = FaqQuestionForm(instance=faq)
    if request.method == 'POST':
        form = FaqQuestionForm(request.POST, instance=faq)
        form.save()
        messages.success(request, "Les modifications ont été enregistrer.")
        return redirect('leads:index-help')   
    context = {
        'faq': faq,
        'form': form,
    }
    return render(request, 'Administration/formulaire-modification-faq.html', context)

@login_required(login_url='/login/')
def AskQuestion(request):
    form = AskQuestionForm()
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid:
            question = form.cleaned_data.get('question')
            type = form.cleaned_data.get('type')

            question = AskQuestion(
                question = question,
                user = request.user,
                type = type,
            )

            question.save()
            messages.success(request,"Votre question à été poser, une réponse vous sera communiquer dans les plus brefs délais.")
            return redirect('leads:index-help')
        else:
            messages.success(request, "Une erreure est survenue lors du traitement de la requete.")
            return redirect('leads:index-help')
    context = {
        'form':form,
    }
    return render(request, 'Administration/poser-une-question.html',context)

@login_required(login_url='/login/')
def MesQuestion(request):
    MaListe = AskQuestion.objects.filter(user = request.user)
    context = {
        'MaListe' : MaListe,
    }

    return render(request, 'Administration/ma-liste-de-question.html', context)
########## FIN DEBUT HELP #####################################

########## DEFINITION DES DROITS D'ACCEES #####################

########## FIN DEFINITION DES DROITS D'ACCEES #################

########## NOT FOUND AND ERROR ################################
def NotFound(request):
    return render(request, 'front/404.html')

def Error(request):
    return render(request, 'front/erreur.html')

########## FIN NOT FOUND AND ERROR ############################

########## GESTION DES RENDEZ VOUS ############################
@login_required(login_url='/login/')
@transaction.atomic
def AjoutRdv(request):
    form = AjoutRdvForm(user = request.user.agent.id_company)
    if request.method == 'POST':
        form = AjoutRdvForm(request.user.agent.id_company, request.POST)
        if form.is_valid():
            status = form.cleaned_data.get('status')
            client = form.cleaned_data.get('client')
            motif = form.cleaned_data.get('motif')
            date_rendez_vous = form.cleaned_data.get('date_rendez_vous')
            observation = form.cleaned_data.get('observation')
            
            rdv = RendezVous(
                created_by = request.user,
                client = client,
                motif = motif,
                date_rendez_vous = date_rendez_vous,
                observation = observation,
                status = status,
                id_comp = request.user.agent.id_company,
            )
            rdv.save()
            messages.success(request, 'Rendez-planier avec succès.')
            return redirect('leads:list-rendez-vous')
        else:
            messages.error(request, 'Une erreur est survenu lors du traitement de la requete, veuillez réessayer !')
            return redirect('leads:ajouter-rendez-vous')
    else:
        context = {
            'form' : form,
        }
        return render(request, 'Administration/rendez_vous/creer-un-rdv.html', context)

@login_required(login_url='/login/')
def DetailsRdv(request, pk):
    rdv = RendezVous.objects.get(id = pk)
    context = {
        'rdv' : rdv,
    }
    return render(request, 'Administration/rendez_vous/details-rdv.html', context)

@login_required(login_url='/login/')
def RemoveRdv(request, pk):
    rdv = RendezVous.objects.get(id = pk)
    rdv.delete()
    messages.success(request, 'Suppression effectuer avec succés.')
    return redirect('leads:list-rendez-vous')

@login_required(login_url='/login/')
def UpdateStatRdv(request):
    pass

@login_required(login_url='/login/')
def UpdateRdv(request, pk):
    rdv = RendezVous.objects.get(id = pk)
    form = AjoutRdvForm(request.user.agent.id_company,instance=rdv)
    if request.method == 'POST':
        form = AjoutRdvForm(request.user.agent.id_company,request.POST, instance=rdv)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mise à jour effectuer avec succés.')
            return redirect('leads:miseajour-rendez-vous', rdv.id)
        else:
            messages.error(request, 'Une erreur est survenue lors de la mise à jours !')
            return redirect('leads:list-rendez-vous', rdv.id)
    else:
        context = {
            'form' : form,
        }
        return render(request, 'Administration/rendez_vous/mise-a-jour-rdv.html', context)

@login_required(login_url='/login/')
def ListRdv(request):
    resultats = RendezVous.objects.all().filter(id_comp = request.user.agent.id_company)
    context = {
        'resultats' : resultats,
    }
    return render(request, 'Administration/rendez_vous/list-des-rdv.html', context)

########## FIN GESTION DES RENDEZ VOUS ########################