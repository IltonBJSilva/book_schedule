from django.http import HttpResponse
from django.shortcuts import render
from plataforma.models import Book

# Create your views here.

def logar(request):
	if request.user.is_authenticated:
		titulo_livro = Book.objects.all()

		return render(request, 'plataforma.html',{'titulo_livro': titulo_livro})
	else:
		return render(request, ' account/login.html')


def salvar(request):
	#capturar os campos
	vtitulo = request.POST.get("titulo")
	vresenha = request.POST.get("resenha")

	Book.objects.create(nome=vtitulo)
	Book.objects.create(resenha=vresenha)

	titulo_livro = Book.objects.all()
	resenha_livro = Book.objects.all()

	return render(request,'plataforma.html', {'titulo_livro': titulo_livro})



