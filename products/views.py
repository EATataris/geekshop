import os

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.conf import settings
from django.core.cache import cache

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


def get_links_category():
   if settings.LOW_CACHE:
       key = 'links_category'
       link_category = cache.get(key)
       if link_category is None:
           link_category = ProductCategory.objects.all()
           cache.set(key, link_category)
       return link_category
   else:
       return ProductCategory.objects.all()


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self):
        category_id = self.kwargs.get('category_id', None)
        if category_id:
            return self.model.objects.filter(category_id=self.kwargs.get('category_id')).select_related('category')
        else:
            return self.model.objects.all().select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'GeekShop - Каталог'
        context['categories'] = get_links_category()
        return context


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


    def get_context_data(self, category_id=None, *args, **kwargs):
        """Добавляем список категорий для вывода сайдбара с категориями на странице каталога"""
        context = super().get_context_data()

        context['product'] = get_product(self.kwargs.get('pk'))
        context['categories'] = ProductCategory.objects.all()
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
