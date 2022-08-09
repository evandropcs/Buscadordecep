from django.urls import path
from cep import views

urlpatterns = [
    path('', views.home, name='home'),
]
