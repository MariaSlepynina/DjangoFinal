from django.forms import ModelForm
from . import models


class ClientForm(ModelForm):
    class Meta:
        model = models.Client
        fields = ['name', 'sity_name']

class TarifForm(ModelForm):
    class Meta:
        model = models.Tarif
        fields = ['name', 'users']

class OperatorForm(ModelForm):
    class Meta:
        model = models.Operator
        fields = ['name', 'tarif', 'client']
