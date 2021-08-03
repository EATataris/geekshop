import os

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic.list import ListView

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


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'GeekShop - Каталог'
        context['categories'] = ProductCategory.objects.all()

        category_id = self.request.GET.get('category_id')
        if category_id:
            products = Product.objects.filter(category_id=category_id)
        else:
            products = Product.objects.all()

        paginator = Paginator(products, self.paginate_by)
        context['products'] = paginator
        return context


# def products(request, category_id=None, page=1):
#     context = {
#         'title': 'GeekShop - Каталог',
#         'categories': ProductCategory.objects.all(),
#     }
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#     else:
#         products = Product.objects.all()
#     paginator = Paginator(products, 3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context['products'] = products_paginator
#     return render(request, 'products/products.html', context)
