from enum import auto
from django.db import models
from django.http import request
from leads.models import User

class Faq(models.Model):
    question = models.CharField(max_length=100, null=True, blank=True)
    response = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name='Foire aux question'
        verbose_name_plural="Foire aux question"

    def __str__(self):
        return self.question

QUESTION_TYPE = (
    ('as','Assistance'),
    ('dm', "Demande d'information"),
)

class AskQuestion(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000, null=True, blank=True)
    type = models.CharField(max_length=2, choices=QUESTION_TYPE, null=True, blank=True)
    reponse = models.CharField(max_length=10000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name=  "Question utilisateur"
        verbose_name_plural = "Questions des utilisateurs"

    def __str__(self):
        return self.user





