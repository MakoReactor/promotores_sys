from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .forms import ContactForm

from .models import Promotora, Cliente, Tasting

class HomePageView(TemplateView):
	template_name = 'home.html'

class PromotoraPageView(ListView):
	model = Promotora
	template_name = 'promotora_list.html'

class PromotoraDetailView(DetailView):
	model = Promotora
	template_name = 'promotora_detail.html'
	context_object_name = 'promotora'

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
	#success_url = reverse_lazy('home')
	success_url = '/thanks/'

class ClienteListView(ListView):
	model = Cliente
	template_name = 'cliente_list.html'

class ThanksTemplateView(TemplateView):
	template_name = 'thanks.html'

class TastinListView(ListView):
	model = Tasting
	template_name = 'tasting_list.html'

class TastinCreateView(CreateView):
	model = Tasting
	template_name = 'tasting_new.html'
	#fields = ['promotora', 'cliente', 'tasting_date']
	fields = '__all__'



#teste Forms
class ContactView(FormView):
	template_name = 'contact.html'
	form_class = ContactForm
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.send_email()
		return super().form_valid(form)
