from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

from . import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 3


class DetelaheProduto(View):

    def get(request, *args, **kwargs):
        return HttpResponse('Detalhe do produto')


class AdicionarCarrinho(View):
    pass


class RemoverCarrinho(View):
    pass


class Carrinho(View):
    pass


class Finalizar(View):
    pass
