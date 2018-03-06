from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .forms import ContactForm

from .models import Promotora, Cliente

class HomePageView(ListView):
	model = Promotora
	template_name = 'home.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'

#teste
class Base2View(TemplateView):
	template_name = 'base2.html'

class PromotoraDetailView(DetailView):
	model = Promotora
	template_name = 'promotora_detail.html'
	context_object_name = 'promotora'

class ClienteListView(ListView):
	model = Cliente
	template_name = 'cliente_list.html'

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

#teste Forms
class ContactView(FormView):
	template_name = 'contact.html'
	form_class = ContactForm
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.send_email()
		return super().form_valid(form)