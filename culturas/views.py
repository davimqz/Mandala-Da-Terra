from django.shortcuts import render

# Create your views here.
def horta_view(request):
    return render(request, 'horta.html')

def saf_view(request):
    return render(request, 'saf.html')

def add_plantacao_view(request):
    return render(request, 'add_plantacao.html')

def painel_view(request):
    return render(request, 'painel.html')