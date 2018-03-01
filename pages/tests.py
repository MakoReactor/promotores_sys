from django.test import TestCase
from django.urls import reverse
from .models import Promotora

class PromotoraModelTest(TestCase):

	def setUp(self):
		Promotora.objects.create(nome="Katia", endereco="rua",
								rg="1",
								cpf="2",
								ctps="3")

	def test_fields_content(self):
		promotora = Promotora.objects.get(id=1)
		expected_object_name = f'{promotora.nome}', f'{promotora.endereco}', f'{promotora.rg}', f'{promotora.cpf}', f'{promotora.ctps}'
		self.assertEqual(expected_object_name, ('Katia', 'rua', "1", "2", "3"))


class HomePageViewTest(TestCase):

	def setUp(self):
		Promotora.objects.create(nome="Katia", endereco="rua",
								rg="1",
								cpf="2",
								ctps="3")
		
	def test_view_url_exists_at_proper_location(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_view_url_by_name(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'home.html')
