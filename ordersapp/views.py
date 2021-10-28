from django.db import transaction
from django.db.models.signals import pre_delete, pre_save
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.dispatch import receiver
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from ordersapp.forms import OrderItemForm
from ordersapp.models import Order, OrderItem
from baskets.models import Basket
from products.models import Product


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True)

class OrderCreate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'GeekShop | Создать заказ'

        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_items = Basket.objects.filter(user=self.request.user)
            if basket_items:
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=basket_items.count())
                formset = OrderFormSet()

                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
                    form.initial['price'] = basket_items[num].product.price
                basket_items.delete()
            else:
                formset = OrderFormSet()

        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super().form_valid(form)

class OrderUpdate(UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'GeekShop | Обновление заказа'

        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
            for form in formset:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price

        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        return super().form_valid(form)


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:list')


class OrderDetail(DetailView):
    model = Order
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Geekshop | Просмотр зказа'
        return context


def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SENT_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))


@receiver(pre_delete, sender=Basket)
@receiver(pre_delete, sender=OrderItem)
def product_quantity_update_delete(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()


@receiver(pre_save, sender=Basket)
@receiver(pre_save, sender=OrderItem)
def product_quantity_update_save(sender, instance, **kwargs):
    if instance.pk:
        instance.product.quantity -= instance.quantity - instance.get_item(int(instance.pk))
    else:
        instance.product.quantity -= instance.quantity
    instance.product.save()


def get_product_price(request, pk):
    if request.is_ajax():
        product = Product.objects.get(pk=pk)
        if product:
            return JsonResponse({'price': product.price})
    return  JsonResponse({'price': 0})