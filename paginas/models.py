from django.db import models

# Create your models here.

class Doar(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, unique=True)
    valor_doacao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome