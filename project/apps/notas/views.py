# apps/notas/views.py
from .models import Nota
from django.shortcuts import render, get_object_or_404, redirect



def anotar(request):
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo', '').strip()  # Remove espaços extras

        # Verifica se o conteúdo não está vazio
        if not conteudo:
            # Se o conteúdo estiver vazio, podemos passar uma mensagem de erro
            return render(request, 'anotar.html', {'erro': 'O conteúdo da anotação não pode ser vazio.'})

        # Se o conteúdo não estiver vazio, cria a nota
        usuario = request.user if request.user.is_authenticated else None
        Nota.objects.create(
            usuario=usuario,
            conteudo=conteudo
        )
        return redirect('notas:anotar')  # Redireciona para a página de anotar após a criação

    # Se a requisição for GET, ou após um POST bem sucedido, exibe as notas
    notas = Nota.objects.filter(usuario=request.user) if request.user.is_authenticated else []
    return render(request, 'anotar.html', {'notas': notas})


# View para editar uma anotação
def editar_nota(request, id):
    # Recupera a anotação com o ID fornecido
    nota = get_object_or_404(Nota, id=id, usuario=request.user)
    
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        # Atualiza o conteúdo da anotação
        nota.conteudo = conteudo
        nota.save()
        return redirect('notas:anotar')  # Redireciona para a página de anotações

    # Exibe o formulário com os dados da anotação
    return render(request, 'editar_nota.html', {'nota': nota})

# apps/notas/views.py
def remover_nota(request, id):
    # Recupera a anotação com o ID fornecido
    nota = get_object_or_404(Nota, id=id, usuario=request.user)
    
    if request.method == 'POST':
        # Remove a anotação do banco de dados
        nota.delete()
        return redirect('notas:anotar')  # Redireciona para a página de anotações

    # Exibe uma confirmação para remover
    return render(request, 'remover_nota.html', {'nota': nota})

def views_meu_perfil(request):
    return render(request, 'meu_perfil.html')

def views_notificacao(request):
    return render(request, 'notificacao.html')

