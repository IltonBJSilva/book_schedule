"""lista_livros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from plataforma import views

urlpatterns = [
	path('', views.listar_livro, name="listar_livro"),
	path('home/', views.logar, name='logar'),
	path('salvar/', views.salvar,name='salvar'),
	path('editar/<int:id>', views.editar, name='editar'),
	path('update/<int:id>', views.update, name='update'),
	path('deletar/<int:id>', views.deletar, name='deletar'),
    
]
