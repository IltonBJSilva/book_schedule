from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from plataforma.models import Book

# Create your views here.

def logar(request):
	if request.user.is_authenticated:
		livros = Book.objects.all()
		livros = Book.objects.filter(liusuario=request.user)

		return render(request, 'plataforma.html',{'livros': livros})
	else:
		return render(request, ' account/login.html')



def salvar(request, data=None):

	#capturar os campos
	vtitulo = request.POST.get("titulo")
	vresenha = request.POST.get("resenha")
	data







	Book.objects.create(liusuario=request.user,nome=vtitulo,resenha=vresenha,data_text=data)

	livros = Book.objects.all()


	return redirect("/libook/home/")

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











