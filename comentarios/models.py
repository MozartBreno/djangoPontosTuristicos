from django.contrib.auth.models import User
from django.db import models
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    resenha = models.TextField()

    def __str__(self):
        return self.usuario.first_name
# Create your models here.
