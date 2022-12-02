from django.shortcuts import render
from templates import *

# Create your views here.
def logar(request):
	return render(request, 'plataforma.html')


