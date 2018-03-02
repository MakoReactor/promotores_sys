from django.views.generic import ListView, TemplateView, DetailView
from .models import Promotora

class HomePageView(ListView):
	model = Promotora
	template_name = 'home.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'

class PromotoraDetailView(DetailView):
	model = Promotora
	template_name = 'promotora_detail.html'
	context_object_name = 'promotora'


