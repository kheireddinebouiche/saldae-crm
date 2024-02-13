
from cProfile import label
from logging import PlaceHolder
from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.enums import Choices, TextChoices
from django.db.models.expressions import F
from django.db.models.fields import FloatField, IntegerField, TextField
from django.db.models.query_utils import select_related_descend
from django.forms.fields import ChoiceField
from .models import *
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import ModelForm, TextInput, EmailInput, widgets
from django.contrib.auth import get_user_model
from produits.models import *
from help.models import *
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import * 

User = get_user_model()

STATUS_DEVIS=  {
    ('env', 'Envoyé'),
    ('acc', 'Accepté'),
    ('Ter', 'Terminé'),
    ('fac', 'Facturé'),
    ('ann', 'Annullé'),
}

USER_TYPE = {
    ('ve', 'Vendeur'),
    ('ag', 'Agent'),
    ('ad', 'Administrateur'),
}

CAT_CLIENT = {
    ('p', 'Personne'),
    ('e', 'Entreprise'),
}

TYPE_FOURNISSEUR = {
    ('pa', 'Paticulier'),
    ('en', 'Entreprise'),
}

class DateInput(forms.DateInput):
    input_type = 'date'

class LeadForm(forms.Form):
    first_name= forms.CharField()
    last_name= forms.CharField()
    age= forms.IntegerField()

class LeadModelForm(ModelForm):
    class Meta:   
        model = Lead
        fields = (
            'agent',
            'first_name' ,
            'last_name', 
            'age',
        )

class CustomAgentCreationForm(UserCreationForm):
    num_identification = forms.CharField(max_length=100, label="N° d'identification : ", required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, label="Type d'utilisateur : ")
    image = forms.ImageField(label="Photo de profile :")
    username = forms.CharField(label="Nom d'utilisateur :")
    first_name= forms.CharField(label="Prénom : ")
    last_name= forms.CharField(label="Nom : ")
    email = forms.EmailField(label="Adresse Email : ", required=True)
   
    class Meta:
      model = User
      fields = ('username','email','first_name','last_name','password1','num_identification', 'user_type', 'image')
      field_classes = {
          'username' : UsernameField, 
        
        }
      widgets = {
          'username' : TextInput(attrs={
              'class' : 'form-control',
              'placeholder': "Veuillez renseignez un nom d'utilisateur.",
          }),
          'email' : EmailInput(attrs={
              'class' : 'form-control',
              'placeholder': "Adresse email de l'utilisateur",
          }),
          'first_name' : TextInput(attrs={
              'class' : 'form-control',
              'placeholder' : 'Prénom',
          }),
          'last_name' : TextInput(attrs={
              'class' : 'form-control',
              'placeholder' : "Nom de famille"
          }),          
      }

class CustomAgentAdmin(UserCreationForm):
    num_identification = forms.CharField(max_length=100)
    user_type = forms.ChoiceField(choices=USER_TYPE)
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','num_identification', 'image')

        field_classes = {
          'username' : UsernameField, 
        
        }
        widgets = {
            'username' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder': "Veuillez renseignez un nom d'utilisateur.",
            }),
            'email' : EmailInput(attrs={
                'class' : 'form-control',
                'placeholder': "Adresse email de l'utilisateur",
            }),
            'first_name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Nom de famille',
            }),
            'last_name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Prénom de l'utilisateur."
            }),

        }

class AgentForm(ModelForm):   
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Nom d'utilisateur",
            }),
            'email' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Email",
            }),
            'first_name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Prénom",
            }),
            'last_name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Nom",
            }),
        }

class AgentProfile(ModelForm):

    class Meta:
        model = Agent
        fields = ('num_identification', 'user_type', 'image')
      
class AgentUpdateProfile(ModelForm):
    class Meta:
        model = Agent
        fields = {'num_identification', 'image'}
        widgets = {
            'num_identification' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'N° d\'identification',
            }),
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta:
      model = User
      fields = ('username',)
      field_classes = {'username' : UsernameField}

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('titre','text_note')
        widgets ={
            'titre' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Donnez un titre à votre note...'
            }),
            'text_note' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Contenu de la note...'
            }),
        }
        labels = {
            'titre' : 'Titre de la note :',
            'text_note' : 'Description de la note :',
        }
      
class ClientForm(ModelForm):  
    class Meta:
        model = Client
        fields = ('raison','adresse','rue','province','pays','zip','gerant','telephone','fax','email','categorie_client','secteur', 'nrc','nif','art')
        widgets = {
            'raison': TextInput(attrs={
                'class': "form-control",
                'placeholder' : "Raison social de l'entreprise/individu.",
                'style' : 'margin: auto;',
            }),
            'secteur' : widgets.Select(attrs={
                'class' : 'form-control',
                'placeholder' : "Secteur d'activité"
            }),
            'adresse': TextInput(attrs={
                'class': "form-control",
                'placeholder' : "Adresse du siege social.",             
            }),
            'rue' : TextInput(attrs={
                'class' : "form-control",
                'placeholder' : "Numéro de rue",
            }),
            'province' : TextInput(attrs={
                'class' : "form-control",
                'placeholder' : "Etat/Province",
            }),
            'pays' : TextInput(attrs={
                'class' : "form-control",
                'placeholder' : "Pays",
            }),
            'zip' : TextInput(attrs={
                'class' : "form-control",
                'placeholder': 'Code ZIP',
            }),
            'gerant': TextInput(attrs={
                'class': "form-control",
                'placeholder' : "Nom/prénom du résponsable.",
                'style' : 'margin: auto;',
                
            }),
            'telephone' : widgets.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Numéro de téléphone/mobile",
                
            }),
            'fax' : widgets.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Fax',
            }),
            'email' : EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Adresse E-mail',
            }),
            'categorie_client' : widgets.Select(attrs={
                'class' : 'form-control',
                'choices' : 'CAT_CLIENT',
            }),
            'nrc' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'N° du registre commerce'
            }),
            'nif' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'N° d\'identification fiscal'
            }),
            'art' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Code article'
            }),

        }

MODE_PAIEMENT ={
    ('Virement', 'Virement'),
    ('Cash', 'Cash'),
    ('Terme', 'A terme'),
}

class DevisForm(ModelForm):
    class Meta:
        model = Devis
        fields = ('prospet','status','observation','date_du_bon','adresse_livraison','methode_paiement')
        widgets = {
            'prospet': widgets.Select(attrs={
                'class' : "form-control",
            }),

            'status': widgets.Select(attrs={
                'class' : "form-control",
                'choices' : "STATUS_DEVIS",
            }),
            'observation': widgets.Textarea(attrs={
                'class' : "form-control",
                'placeholder' : "Observation - max 2000",
                
            }),
            'date_du_bon' : DateInput(attrs={
                'class' : 'form-control',
            }),
            'adresse_livraison' : TextInput(attrs={
                'class' : 'form-control',
            }),
            'methode_paiement' : widgets.Select(attrs={
                'class' : 'form-control',
                'choices' : 'MODE_PAIEMENT',
            }),
        }

class ProduitsDevisForm(ModelForm):
    class Meta:
        model = ProduitsDevis
        fields = ('product','qtr','prix','remise')

        widgets = {
            'product' : widgets.Select(attrs={
                'class' : 'form-control',
            }),
            'qtr' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Quantité produits/service'
            }),
            'prix' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'step' : '0.01',
                'placeholder' : 'Prix du produit/service'
            }),
            'remise' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'step' : '0.01',
                'placeholder': 'Remise sur le produit/service en %',
            })
           
            
        }
     
PRIORITY = {
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
}
STATUS_TACHE= {
    ('aff', 'A faire'),
    ('enc', 'En cours'),
    ('ter', 'Terminé'),
    ('enp', 'En pause'),
    ('ann', 'Annulé'),
}
    

class FournisseursForm(ModelForm):
    class Meta:
        model = Fournisseurs
        fields = ('raison','secteur','adresse','pays','province','zip','rue','mobile','telephone','email','fournisseur_type','nis','nif','art','rc')
        widgets = {
            'raison' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'Raison social'
            }),
            'adresse' : widgets.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Adresse',
                'style': 'height: 100px;',
            }),
            'pays' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'Pays'
            }),
            'province' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'Etat/province'
            }),
            'zip' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'Zip'
            }),
            'rue' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'N° de rue'
            }),
            'mobile' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'N° Téléphone mobile'
            }),
            'telephone' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'N° Téléphone'
            }),
            'email' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'E-mail'
            }),
            'fournisseur_type' : widgets.Select(attrs={
                'class' : 'form-control',
                'choices' : 'TYPE_FOURNISSEUR'
            }),
            'nif' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'NIF'
            }),
            'nis' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'NIS'
            }),
            'art' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'ARTICLE'
            }),
            'rc' : TextInput(attrs={
                'class'  : 'form-control',
                'placeholder' : 'N° Registre commerce'
            }),
            'secteur' : widgets.Select(attrs={
                'class' : 'form-control',
                
            }),
            
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = {'sujet','messages','nom'}
        widgets = {
            'sujet' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Sujet",
            }),
            'messages' : widgets.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Votre message',
            }),
            'nom' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Votre nom'
            })
        }

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class DropDownDevisState(forms.Form):
   
    favorite_colors = forms.Select(
        
        
        choices=FAVORITE_COLORS_CHOICES,
    )

class SecteurActiviteForm(ModelForm):
    class Meta:
        model = SecteurActivite
        fields = {'libelle'}
        widgets = {
            'libelle' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder': "Secteur d'activité",
            }),
        }

class FaqQuestionForm(ModelForm):
    class Meta:
        model= Faq
        fields = {'question','response'}
        widgets = {
            'question' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Veuillez saisir une question."
            }),
            'response' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Veuillez renseigner une reponse',
            }),
        }

QUESTION_TYPE = (
    ('as','Assistance'),
    ('dm', "Demande d'information"),
)

class AskQuestionForm(ModelForm):
    class Meta:
        model = AskQuestion
        fields = {'question','type'}
        widgets = {
            'question' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder': "Veuillez saisir votre question."
            }),
            'type' : widgets.Select(attrs={
                'choices' : 'QUESTION_TYPE',
                'class' : 'form-control',
            })
        }

class BookModelForm(BSModalModelForm):
    class Meta:
        model = Note
        fields = ['text_note']

class TachesForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(TachesForm, self).__init__(*args, **kwargs)
        self.fields['assigner'].queryset = Agent.objects.all().filter(id_company=user)
        self.fields['client'].queryset = Client.objects.all().filter(id_comp=user)
        
    class Meta:
        model = Tache
        fields = ('sommaire','description','assigner','date_debut','date_fin','status','client','priorite')
        widgets = {
            'sommaire' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Sommaire'
            }),

            'description':  forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Déscription de la tâche',
            }),
            
            'status' : widgets.Select(attrs={
                'class' : 'form-control',
                'choices' : 'STATUS_TACHE',
            }),
            
            'date_debut' : DateInput(attrs={
                'class' : 'form-control'
            }),
            'date_fin' : DateInput(attrs={
                'class' : 'form-control'
            }),

            'priorite' : widgets.Select(attrs={
                'class' : 'form-control',
                'choices' : 'PRIORITY',
            }),

            'client' : widgets.Select(attrs={
                'class' : 'form-control',
            }),
            'assigner' : widgets.Select(attrs={
                'class' : 'form-control',
            }),
        
        }

class AssignTachForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(AssignTachForm, self).__init__(*args, **kwargs)
        self.fields['assigner'].queryset = Agent.objects.all().filter(id_company=user)
        self.fields['client'].queryset = Client.objects.all().filter(id_comp=user)

    class Meta:
        model = Tache
        fields = ('assigner', 'client')
    
RDV_STATUS={
    ('con', 'Confirmé'),
    ('ann', 'Annulé'),
    ('att', 'En attante')
    
}

class AjoutRdvForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(AjoutRdvForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.all().filter(id_comp=user)

    class Meta:
        model = RendezVous
        fields = ('client','date_rendez_vous','status','motif','observation')
        widgets = {
            'client' : forms.Select(attrs={
                'class' : 'form-control',
                
            }),

            'date_rendez_vous' : DateInput(attrs={
                'class' : 'form-control',

            }),

            'status' : forms.Select(attrs={
                'choices' : 'RDV_STATUS',
                'class' : 'form-control',
            }),

            'motif' : forms.TextInput(attrs={
                'class' : 'form-control',
                
            }),
            'observation' : forms.Textarea(attrs={
                'class' : 'form-control',
            }),
        }

        labels = {
            'client': "Client : *",
            'date_rendez_vous' : "Date du rendez-vous :*",
            'status' : "Status du rendez-vous : *",
            'motif': "Motif(s) : ",
            'observation' : "Observations :"

        }


        