import datetime
import os
import json

from django.shortcuts import render

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

def products(request):
    file_path = os.path.join(MODULE_DIRS, 'fixtures/goods.json')
    context = {
        'title': 'GeekShop - Каталог',
        'cur_date': datetime.datetime.now(),
        'products': json.load(open(file_path, encoding='utf-8'))
    }
    return render(request, 'products/products.html', context)
