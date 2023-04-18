import datetime

from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from .models import Post


def telaprincipal(request):
    return render(request, 'telaPrincipal.html')
def inicio(request):
    # return render(request,'index.html')
    listposts = Post.objects.all()
    if not listposts:
        return render(request, 'index.html')
    else:
        return render(request, 'index.html', {"posts":listposts})

def causas(request):
    return render( request,'causas.html')
def consequencias(request):
    return render(request,'consequencias.html')
def solucoes(request):
    return render(request,'solucoes.html')

def newpost(request):
    p_autor = request.POST.get('autor')
    p_title = request.POST.get('title')
    p_txt = request.POST.get('coment')
    publicado = datetime.date.today()


    try:
         post = Post(autor=p_autor, titulo=p_title, comentario=p_txt,data=publicado)
         post.save()
         return redirect('/index/')
    except:
            messages.add_message(request, constants.ERROR, 'Erro no cadastro')
            return redirect('/app/index/')
    return HttpResponse(f"{autor}, {titulo}, {comentario}, {data}")


def editar(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'editpost.html', {"post":post})

def atualizar_post(request, id):

    p_titulo = request.POST.get("title")
    p_autor = request.POST.get("autor")
    p_comentario = request.POST.get("coment")

    publicado = datetime.date.today()

    post = Post.objects.get(id=id)
    post.data= publicado

    if p_titulo != "":
        post.titulo=p_titulo
    if p_comentario != "":
        post.titulo=p_comentario
    if p_autor != "":
        post.titulo=p_autor

    post.save()
    listpost = Post.objects.all()
    return render(request,'index.html', {"posts": listpost})

def apagar_post(request, id):
    usuario = Post.objects.get(id=id)
    usuario.delete()
    listpost= Post.objects.all()

    return redirect('/app/index/')
