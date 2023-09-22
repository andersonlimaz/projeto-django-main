from django import forms
from django.db import models


class Doador(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    valor_doacao = models.DecimalField(max_digits=10, decimal_places=2)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    cpf = models.CharField(max_length=14)

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['valor_doacao', 'nome', 'email', 'sexo', 'data_nascimento', 'telefone', 'cpf']

