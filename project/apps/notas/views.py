from django.shortcuts import render, redirect, get_object_or_404
from . models import Nota
from django.contrib.auth.decorators import login_required

@login_required
def views_lista_notas(request):
    notas = Nota.objects.filter(usuario=request.user)
    
    for nota in notas:
        nota.conteudo_exibido = nota.conteudo[:35] + ('...' if len(nota.conteudo) > 100 else '')
        
    return render(request, 'lista_notas.html', {'notas': notas})

@login_required
def views_nova_nota(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        nota = Nota(titulo=titulo, conteudo=conteudo, usuario=request.user)
        nota.save()
        return redirect('notas:lista_notas')
    return render(request, 'nova_nota.html')

@login_required
def views_editar_nota(request, id):
    nota = get_object_or_404(Nota, id=id, usuario=request.user)
    if request.method == 'POST':
        nota.titulo = request.POST.get('titulo')
        nota.conteudo = request.POST.get('conteudo')
        nota.save()
        return redirect('notas:lista_notas')
    return render(request, 'editar_nota.html', {'nota': nota})

@login_required
def views_deletar_nota(request, nota_id):
    if request.method == 'POST':
        nota = get_object_or_404(Nota, id=nota_id)
        nota.delete()
        return redirect('notas:index')  # Redireciona para a página de índice das notas
    else:
        return redirect('notas:index')  # Redireciona se não for um POST

def views_confirmar_deletar(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    nota.delete()
    return redirect('notas:lista_notas')

def views_ver_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    return render(request, 'ver_nota.html', {'nota': nota})

def views_notificacao(request):
    return render(request, 'notificacao.html')

def views_meu_perfil(request):
    return render(request, 'meu_perfil.html')