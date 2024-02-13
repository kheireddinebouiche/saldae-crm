from django.db import transaction
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

@login_required(login_url='/login/')
@transaction.atomic
def CreateMyCompany(request):
    form = AddCompanyForm()
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            designation = form.cleaned_data.get('designation')
            nif = form.cleaned_data.get('nif')
            art = form.cleaned_data.get('art')
            nrc = form.cleaned_data.get('nrc')
            adresse1 = form.cleaned_data.get('adresse1')
            nrue = form.cleaned_data.get('nrue')
            province = form.cleaned_data.get('province')
            etat = form.cleaned_data.get('etat')
            email = form.cleaned_data.get('email')
            telephone = form.cleaned_data.get('telephone')
            mobile = form.cleaned_data.get('mobile')
            fax = form.cleaned_data.get('fax')

            company = MyCompany(
                designation = designation,
                nif = nif,
                art = art,
                nrc = nrc,
                adresse1 = adresse1,
                nrue = nrue,
                province = province,
                etat  = etat, 
                email = email,
                telephone = telephone,
                mobile = mobile,
                fax = fax,
                gestionnaire = request.user.agent
                
            )

            company.save()
            messages.success(request, "Les informations de votre entreprise ont été enregistrer.")
            return redirect('mycompany:check-for-admin')
        else:
            messages.error(request, "Une erreure c'est produite lors du traitement de la requete.")
            return redirect('mycompany:configurer-mon-entreprise')
    context = {
        'form' : form,
    }
    return render(request, 'Administration/configurer-mon-entreprise.html', context)

@login_required(login_url='/login/')      
def AlterMyCompany(request, pk):
    mycompany = MyCompany.objects.get().last()

    context = {
        'mycompany' : mycompany,
    }

    return render(request, 'Administration/modifier-mon-entreprise.html', context)

def DropMyCompany(request, pk):
    pass

@login_required(login_url='/login/')
def ShowMyCompany(request):

    mycompany = MyCompany.objects.filter(gestionnaire = request.user)
    context = {
        'mycompany': mycompany,
    }
    return render(request, 'Administration/infos-mon-entreprise.html', context)
   

@login_required(login_url='/login/')
def CheckForAdmin(request):
    admin = Agent.objects.filter(user_type = 'ad')
    if admin:      
        return redirect('leads:Administration')
    else:
        return redirect('leads:create-admin')


### Souscription à un abonnement
@transaction.atomic
def freePlan(request):
    form = AccountCreation()
    form1 = CompanyForm()
    if request.method == 'POST':
        form = AccountCreation(request.POST)
        form1 = CompanyForm(request.POST)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.refresh_from_db()

            designation = form1.cleaned_data.get('designation')

            comp = MyCompany(
                designation = designation,
                niveau = 'free',
                gestionnaire = user.agent.user,
            )
            comp.save()

            user.agent.id_company = comp.id
            user.agent.has_company = True
            user.agent.user_type = 'ad'
            
            user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('landing_page')
        else:
            return redirect('leads:erreur')
    else:
        context = {
            'form' : form,
            'form1' : form1,
        } 
        return render(request, 'front/souscription.html', context)


    form = AccountCreation()
    form1 = CompanyForm()
    if request.method == 'POST':
        form = AccountCreation(request.POST)
        form1 = CompanyForm(request.POST)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.refresh_from_db()

            designation = form1.cleaned_data.get('designation')

            comp = MyCompany(
                designation = designation,
                niveau = 'pro',
                gestionnaire = user.agent.user,
            )
            comp.save()

            user.agent.id_company = comp.id
            user.agent.has_company = True
            user.agent.user_type = 'ad'
            
            user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('landing_page')
        else:
            return redirect('leads:erreur')
    else:
        context = {
            'form' : form,
            'form1' : form1,
        } 
        return render(request, 'front/souscription.html', context)