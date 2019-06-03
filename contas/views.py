from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Transacao
from .forms import TransacaoForm


# Create your views here.
def home(request):  # READ
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()

    # html = "<html><body>it is now %s</body></html>" % now
    return render(request, 'contas/home.html', data)


def listagem(request):  # READ
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):  # CREATE
    data = {}
    form = TransacaoForm(request.POST or None)  # o Django procura se ja tem os campos com a informação preenchida

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)


def update(request, pk):  # UPDATE
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
