from django.db import models

class Promotora(models.Model):
	nome = models.CharField(max_length=100)
	endereco = models.CharField(max_length=100)
	rg = models.CharField(max_length=100)
	cpf = models.CharField(max_length=100)
	ctps = models.CharField(max_length=100)

	def __str__(self):
		"""Representação de um modelo"""
		return self.nome
