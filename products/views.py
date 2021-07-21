import datetime
import os
import json

from django.shortcuts import render
from .models import ProductCategory, Product
# Create your views here.

MODULE_DIRS = os.path.dirname(__file__)

def index(request):
    context = {
        'title': 'GeekShop',
        'promotion': True,
        'promotion_text': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'no_promo_text': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру!',

    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        context['products'] = Product.objects.filter(category_id=category_id)
    else:
        context['products'] = Product.objects.all()
    return render(request, 'products/products.html', context)
