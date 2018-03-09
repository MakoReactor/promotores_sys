from django.urls import path
from django.views.i18n import JavaScriptCatalog

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('promotora/', views.PromotoraPageView.as_view(), name='promotora_list' ),
    path('promotora/<int:pk>/', views.PromotoraDetailView.as_view(), name='promotora_detail'),
    path('promotora/new/', views.PromotoraCreateView.as_view(), name='promotora_new'),
    path('promotora/<int:pk>/edit/', views.PromotoraUpdateView.as_view(), name='promotora_edit'),
    path('promotora/<int:pk>/delete/', views.PromotoraDeleteView.as_view(), name='promotora_delete'),
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('contato/', views.ContactView.as_view(), name='contact'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thanks'),
    path('tasting', views.TastinListView.as_view(), name='tasting_list'),
    path('tasting/new/', views.TastinCreateView.as_view(), name='tasting_new'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
