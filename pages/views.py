from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


#Forms
class PromotoraCreateView(CreateView):
	model = Promotora
	template_name = 'promotora_new.html'
	fields = '__all__'

class PromotoraUpdateView(UpdateView):
	model = Promotora
	fields = '__all__'
	template_name = 'promotora_edit.html'

class PromotoraDeleteView(DeleteView):
	model = Promotora
	template_name = 'promotora_delete.html'
	success_url = reverse_lazy('home')