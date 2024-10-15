from django.shortcuts import render

def HomeView(request):
    return render (request, 'home.html')

def SafView(request):
    return render (request, 'saf.html')

def HortaView(request):
    return render (request, 'horta.html')

def AdicionarPlantacaoView(request):
    return render (request, 'adicionar_plantacao.html')