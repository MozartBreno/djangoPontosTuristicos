from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    listaComentario = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderenco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    imagem = models.ImageField(upload_to='pontosTuristicos', null=True, blank=True)

    def __str__(self):
        return self.nome
