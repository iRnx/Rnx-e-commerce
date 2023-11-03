from django.contrib import admin
from .models import ItemPedido, Pedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]




admin.site.register(ItemPedido)
