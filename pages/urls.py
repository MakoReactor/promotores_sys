from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('sobre/', views.AboutPageView.as_view(), name='about'),
    path('promotora/<int:pk>/', views.PromotoraDetailView.as_view(), name='promotora_detail'),
    path('promotora/new/', views.PromotoraCreateView.as_view(), name='promotora_new'),
    path('promotora/<int:pk>/edit/', views.PromotoraUpdateView.as_view(), name='promotora_edit'),
    path('promotora/<int:pk>/delete/', views.PromotoraDeleteView.as_view(), name='promotora_delete'),
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list')
]