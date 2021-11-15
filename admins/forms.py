from django import forms
from products.models import Product, ProductCategory

from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))


class ProductAdminCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите название продукта'}))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите описание'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите цену'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите количество'}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), widget=forms.Select(attrs={
        'style': 'border: 1px solid #ced4da; border-radius: 0.25rem; display: flex; min-width: 100%;'}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category')


class CategoryAdminCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите название категории'}))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите описание'}))
    discount = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4'}), required=False, initial=0, min_value=0, max_value=90)

    class Meta:
        model = ProductCategory
        fields = ('name', 'description', 'discount')