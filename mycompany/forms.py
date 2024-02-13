from django import forms
from django.db.models.base import Model
from django.db.models.enums import Choices, TextChoices
from django.db.models.expressions import F
from django.db.models.fields import FloatField, IntegerField, TextField
from django.db.models.query_utils import select_related_descend
from django.forms.fields import ChoiceField
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth import get_user_model
from leads.models import *


class AddCompanyForm(ModelForm):
    class Meta:
        model = MyCompany
        fields= ('designation','nif','art','nrc','adresse1','nrue','province','etat','email','telephone','mobile','fax')
        widgets = {
            'designation' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Entrez la designation de votre entreprise',
                'style' : 'color:black',
            }),
            'nif' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Numéro d'identification fiscal",
                'style' : 'color:black',
            }),
            'art' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Numéro d'article",
                'style' : 'color:black',
            }),
            'nrc' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Numéro du registre commerce',
                'style' : 'color:black',
            }),
            'adresse1' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Votre adresse',
                'style' : 'color:black',
            }),
            'nrue' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Rue',
                'style' : 'color:black',
            }),
            'province' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Province',
                'style' : 'color:black',
            }),
            'etat' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Pays',
                'style' : 'color:black',
            }),
            'email' : EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Votre adresse Email',
                'style' : 'color:black',
            }),
            'telephone' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Numéro de téléphone',
                'style' : 'color:black',
            }),
            'mobile' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Votre numéro de mobile',
                'style' : 'color:black',
            }),
            'fax' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Votre numéro de fax',
                'style' : 'color:black',
            }),
        }

class AccountCreation(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class CompanyForm(ModelForm):
    class Meta:
        model = MyCompany
        fields = {'designation'}
        widgets = {
            'designation' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Entrez la designation de votre entreprise',
                      
            }),            
        }