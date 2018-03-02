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

	def test_string_represetation(self):
		promotora = Promotora(nome='katia')
		self.assertEqual(str(promotora), promotora.nome)

	def test_post_content(self):
		self.promotora = Promotora.objects.get(id=1)
		self.assertEqual(f'{self.promotora.nome}', 'Katia')
		self.assertEqual(f'{self.promotora.endereco}', 'rua')
		self.assertEqual(f'{self.promotora.rg}', '1')
		self.assertEqual(f'{self.promotora.cpf}', '2')
		self.assertEqual(f'{self.promotora.ctps}', '3')

	def test_promotora_detail_view(self):
		response = self.client.get('/promotora/1/')
		no_response = self.client.get('/promotora/1000/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'Katia')
		self.assertTemplateUsed(response, 'promotora_detail.html')



class AboutViewTest(TestCase):

	def test_about_page_view(self):
		resp = self.client.get(reverse('about'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'about.html')