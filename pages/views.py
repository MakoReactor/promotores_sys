from django.views.generic import ListView, TemplateView
from .models import Promotora

class HomePageView(ListView):
	model = Promotora
	template_name = 'home.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'

