
from django import forms
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
    num_identification = forms.CharField(max_length=100)
    user_type = forms.ChoiceField(choices=USER_TYPE)
    image = forms.ImageField()
   
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

class AgentProfile(ModelForm):

    class Meta:
        model = Agent
        fields = ('num_identification', 'user_type', 'image')
      
class CustomUserCreationForm(UserCreationForm):

    class Meta:
      model = User
      fields = ('username',)
      field_classes = {'username' : UsernameField}

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = {'text_note'}
        widgets ={
            'text_note' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Contenu de la note...'
            }),
        }
      
class ClientForm(ModelForm):  
    class Meta:
        model = Client
        fields = {'raison','adresse','rue','province','pays','zip','gerant','telephone','fax','email','categorie_client'}
        widgets = {
            'raison': TextInput(attrs={
                'class': "form-control",
                'placeholder' : "Raison social de l'entreprise/individu.",
                'style' : 'margin: auto;',
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
        }

MODE_PAIEMENT ={
    ('Virement', 'Virement'),
    ('Cash', 'Cash'),
    ('Terme', 'A terme'),
}

class DevisForm(ModelForm):
    class Meta:
        model = Devis
        fields = {'prospet','status','observation','date_du_bon','adresse_livraison','methode_paiement'}
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
        fields = {'product','qtr','prix','remise'}

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
    
class TachesForm(ModelForm):
    class Meta:
        model = Tache
        fields = {'sommaire','description','assigner','date_debut','date_fin','status','client','priorite'}
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