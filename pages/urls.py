from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='about'),
    path('home/', views.AboutPageView.as_view(), name='home'),
    path('promotora/<int:pk>/', views.PromotoraDetailView.as_view(), name='promotora_detail'),
    path('promotora/new/', views.PromotoraCreateView.as_view(), name='promotora_new'),
    path('promotora/<int:pk>/edit/', views.PromotoraUpdateView.as_view(), name='promotora_edit'),
    path('promotora/<int:pk>/delete/', views.PromotoraDeleteView.as_view(), name='promotora_delete'),
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('contato/', views.ContactView.as_view(), name='contact'),
    path('base2/', views.Base2View.as_view(), name='base2'),
]