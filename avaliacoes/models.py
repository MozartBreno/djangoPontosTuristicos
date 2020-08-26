from django.contrib.auth.models import User
from django.db import models
class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    nota = models.DecimalField(decimal_places=2,max_digits=10)
    resenha = models.TextField()

    def __str__(self):
        return self.usuario.first_name
# Create your models here.
