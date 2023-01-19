from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Book(models.Model):
	#Criar um model
	liusuario = models.ForeignKey(User, on_delete=models.CASCADE)

	nome = models.CharField(max_length=100)
	resenha = models.CharField(max_length=100)

	data_text = models.DateField('data', auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.nome