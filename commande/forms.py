from django.forms import ModelForm
from django import forms

def  CreatCommand(forms.ModelForm):
    class Meta:
        model = BonDeCommande
        fields = {}