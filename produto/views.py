from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib import messages

from . import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 3


class DetelaheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'  
    slug_url_kwarg = 'slug'
    

class AdicionarCarrinho(View):
    def get(self, *args, **kwargs):

        http_referer = self.request.META.get('HTTP_REFERER', reverse('produto:lista'))
        vid = self.request.GET.get('vid')

        if not vid:
            messages.error(self.request, 'Produto não existe')
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=vid)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if vid in carrinho:
            pass

        return HttpResponse('Adicionar ao carrinho')


class RemoverCarrinho(View):
    pass


class Carrinho(View):
    pass


class Finalizar(View):
    pass
