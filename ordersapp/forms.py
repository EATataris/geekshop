from django import forms
from ordersapp.models import Order, OrderItem
from products.models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderItemForm(forms.ModelForm):
    price = forms.CharField(label='цена', required=False, widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = OrderItem
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all().select_related()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'