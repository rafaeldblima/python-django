from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    # email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name="perfil", on_delete=models.CASCADE)
    
    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado).save()
    # somente se herdar de object
    # def __init__(self, nome='', email='', telefone='', nome_empresa=''):
    #     self.nome = nome
    #     self.email = email
    #     self.telefone = telefone
    #     self.nome_empresa = nome_empresa


class Convite(models.Model):
    solicitante = models.ForeignKey(
        Perfil, related_name='convites_feitos', on_delete=models.PROTECT)
    convidado = models.ForeignKey(
        Perfil, related_name='convites_recebidos', on_delete=models.PROTECT)

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()
