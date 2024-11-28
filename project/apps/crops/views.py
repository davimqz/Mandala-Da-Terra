# views.py
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def pragas(request):
    return render(request, 'praga.html')


# Lista todas as tarefas
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

from django.urls import reverse

import requests
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Task

def home_view(request):
    # Parte 1: Dados Meteorológicos
    api_key = settings.OPENWEATHERMAP_API_KEY
    city = request.GET.get('city', 'Carpina')

    # URL da API para obter o tempo atual
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt&units=metric"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados_meteorologicos = resposta.json()
        temperatura = round(dados_meteorologicos["main"]["temp"])
        descricao = dados_meteorologicos["weather"][0]["description"]
        umidade = dados_meteorologicos["main"]["humidity"]
        velocidade_vento = dados_meteorologicos["wind"]["speed"]
        icon_code = dados_meteorologicos["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    else:
        temperatura = "N/A"
        descricao = "Não disponível"
        umidade = "N/A"
        velocidade_vento = "N/A"
        icon_url = ""

    # Parte 2: Obter tarefas
    tasks = Task.objects.all()

    # Contexto para o template
    contexto = {
        "cidade": city,
        "temperatura": temperatura,
        "descricao": descricao,
        "umidade": umidade,
        "velocidade_vento": velocidade_vento,
        "icon_url": icon_url,
        "tasks": tasks,
    }

    return render(request, 'home.html', contexto)


from datetime import datetime, timedelta
from .models import Task, Cultura

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Nome da cultura
        description = request.POST.get('description')
        rua = request.POST.get('rua')
        completed = 'completed' in request.POST
        data_plantio_str = request.POST.get('data_plantio')  # Data de plantio do formulário

        # Converte a data de plantio para o formato correto
        if data_plantio_str:
            data_plantio = datetime.strptime(data_plantio_str, "%Y-%m-%d").date()
        else:
            data_plantio = None
        
        # Busca o tempo de colheita da cultura
        cultura = Cultura.objects.filter(nome=title).first()  # Busca a cultura pelo nome
        if cultura and data_plantio:
            # Calcula a previsão de colheita
            data_colheita = data_plantio + timedelta(days=cultura.tempo_colheita_dias)
        else:
            data_colheita = None

        # Cria a nova tarefa com ambas as datas
        Task.objects.create(
            title=title,
            description=description,
            rua=rua,
            completed=completed,
            data_plantio=data_plantio,
            data_colheita=data_colheita
        )
        
        return redirect('crops:home')  # Redireciona após a criação

    return render(request, 'task_create.html')




def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect(reverse('crops:home'))

    
    return render(request, 'task_edit.html', {'task': task})
 

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def task_delete(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return JsonResponse({'success': True})  # Retorna sucesso
    return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=405)




from django.shortcuts import render
from .models import Cultura, PlantaCompanheira

def pesquisar_cultura(request):
    # Inicializa a lista de culturas e plantas companheiras
    culturas = Cultura.objects.all()
    plantas_companheiras = []

    if request.method == 'GET' and 'title' in request.GET:
        # Se a cultura foi escolhida, busca as plantas companheiras
        cultura_nome = request.GET.get('title')
        try:
            cultura = Cultura.objects.get(nome=cultura_nome)
            plantas_companheiras = PlantaCompanheira.objects.filter(cultura=cultura)
        except Cultura.DoesNotExist:
            plantas_companheiras = []

    return render(request, 'pesquisar_cultura.html', {
        'culturas': culturas,
        'plantas_companheiras': plantas_companheiras
    })



def detalhes_cultura(request, cultura_id):
    cultura = get_object_or_404(Cultura, id=cultura_id)
    companheiras = cultura.companheiras.all()  # Obtém as plantas companheiras
    return render(request, 'detalhes_cultura.html', {'cultura': cultura, 'companheiras': companheiras})






def pragas(request):
    return render(request, 'praga.html')

def caramujo(request):
    return render(request, 'pragas/caramujo.html')

def lagarta(request):
    return render(request, 'pragas/lagarta.html')

def tomate(request):
    return render(request, 'plantas/tomate.html')





