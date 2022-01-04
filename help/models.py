from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=100, null=True, blank=True)
    response = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name='Foire aux question'
        verbose_name_plural="Foire aux question"

    def __str__(self):
        return self.question
    




