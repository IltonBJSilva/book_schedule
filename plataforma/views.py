from django.http import HttpResponse
from django.shortcuts import render, redirect
from plataforma.models import Book

# Create your views here.

def logar(request):
	if request.user.is_authenticated:
		livros = Book.objects.all()

		return render(request, 'plataforma.html',{'livros': livros})
	else:
		return render(request, ' account/login.html')


def salvar(request):
	#capturar os campos
	vtitulo = request.POST.get("titulo")
	vresenha = request.POST.get("resenha")

	Book.objects.create(nome=vtitulo,resenha=vresenha)
	# Book.objects.create()

	livros = Book.objects.all()
	# resenha_livro = Book.objects.all()

	return render(request,'plataforma.html', {'livros': livros})

def editar(request, id):
	livros = Book.objects.get(id=id)
	return render(request,'update.html', {'livros': livros})


def update(request, id):
	vtitulo = request.POST.get("titulo")
	vresenha = request.POST.get("resenha")


	livro = Book.objects.get(id=id)


	livro.nome = vtitulo
	livro.resenha = vresenha

	livro.save()

	return redirect(logar)


def deletar(request, id):
	livro = Book.objects.get(id=id)
	livro.delete()
	return redirect(logar)











