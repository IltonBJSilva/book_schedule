from datetime import datetime
from django.contrib.messages import constants
from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import render, redirect
from plataforma.models import Book
from django.core.mail import send_mail
import pyttsx3



# Create your views here.

def logar(request):
	if request.user.is_authenticated:
		livros = Book.objects.all()
		livros = Book.objects.filter(liusuario=request.user)
		nome_usuario = request.user.username

		if not request.session.get('usuario_logado', False):
			print("d")
			request.session['usuario_logado'] = True
			texto = f"Usuário {nome_usuario} logado com sucesso"
			engine = pyttsx3.init()
			engine.setProperty('rate', 150)
			engine.say(texto)
			engine.runAndWait()




		return render(request, 'plataforma.html',{'livros': livros})
	else:
		return render(request, ' account/login.html')



def salvar(request, data=None):
	#capturar os campos
	vtitulo = request.POST.get("titulo")
	vresenha = request.POST.get("resenha")

	Book.objects.create(liusuario=request.user,nome=vtitulo,resenha=vresenha,data_text=data)
	livros = Book.objects.all()
	return redirect("/libook/home/")

def editar(request, id):
	livros = Book.objects.get(id=id)
	return render(request,'update.html', {'livros': livros})


def listar_livro(request):
	if request.method == "GET":
		book = request.GET.get('livro')

		livros = Book.objects.filter(nome=book)
		# livros = Book.objects.all()


		# caso o usuario digite algum livro
		if book:
			# icotains e não precisa digitar o nome inteiro da cidade, encontra so com algumas letras
			livros = livros.filter(nome__icontains=book)
			print(livros)


		return render(
			request,
			'plataforma.html',
			{'livros': livros,}
		)

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











