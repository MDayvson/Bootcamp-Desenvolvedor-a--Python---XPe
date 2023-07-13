from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField('nome', max_length=30)
    telefone = models.CharField('telefone', max_length=20)
    email = models.EmailField('email', max_length=30)

    def __str__(self) -> str:
        return f'Nome: {self.nome}, Telefone:{self.telefone}, Email:{self.email}'