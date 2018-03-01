from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('sobre/', views.AboutPageView.as_view(), name='about'),
]