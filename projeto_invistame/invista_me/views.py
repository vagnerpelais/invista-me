from django.shortcuts import render, redirect, HttpResponse # renderiza uma página html, redireciona e retorna um http response
from .models import Investimento # importando a model
from .forms import InvestimentoForm # importando o model form


# creating views
def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', context=dados)


def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)


def criar(request):
    #POST
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        #GET
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    #GET
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    #POST
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')
    


def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})