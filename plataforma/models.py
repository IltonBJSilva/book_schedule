from django.db import models

# Create your models here.
class Book(models.Model):
	#Criar um model
	nome = models.CharField(max_length=100)
	resenha = models.CharField(max_length=100)

	data_text = models.DateField('data', null=True, blank=True)

	def __str__(self):
		return self.nome