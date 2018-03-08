from django.db import models
from django.urls import reverse

class Promotora(models.Model):
	nome = models.CharField(max_length=100)
	endereco = models.CharField(max_length=100)
	rg = models.CharField(max_length=100)
	cpf = models.CharField(max_length=100)
	ctps = models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('promotora_detail', args=[str(self.id)])

	def __str__(self):
		"""Representação de um modelo"""
		return self.nome

class Cliente(models.Model):
	codigo = models.IntegerField(unique=True)
	razao_social = models.CharField(max_length=100)
	fantasia = models.CharField(max_length=100)
	rua = models.CharField(max_length=100)
	bairro = models.CharField(max_length=100)
	cidade = models.CharField(max_length=100)
	cep = models.CharField(max_length=100)

	def get_absolute_url(self):
		pass

	def __str__(self):
		return self.fantasia

class Tasting(models.Model):
	promotora = models.ForeignKey(Promotora, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	tasting_date = models.DateField('Data da Degustação', auto_now_add=False)

	class Meta:
		ordering = ['-tasting_date']


	def get_absolute_url(self):
		return reverse('tasting_list')


	def __str__(self):
		return str(self.promotora)
