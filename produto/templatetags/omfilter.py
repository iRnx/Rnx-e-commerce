from django.template import Library
from utils import utils

register = Library()


@register.filter('formata_preco')
def formata_preco(value):
    return utils.formata_preco(value)