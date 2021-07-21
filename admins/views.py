from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from admins.forms import UserAdminRegistationForm, UserAdminProfileForm, ProductAdminCreationForm, ProductAdminCategoryForm
from users.models import User
from products.models import Product, ProductCategory
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.
@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistationForm
    success_url = reverse_lazy('admins:admin_users')
    template_name = 'admins/admin-users-create.html'



@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'Админ-панель - редактирование пользователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_remove(request, pk):
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_staff)
def admin_products(request):
    context = {'title': 'Админ-панель - продукты', 'products': Product.objects.all()}
    return render(request, 'admins/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductAdminCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminCreationForm()

    context = {
        'title': 'Админ-панель - создание нового продукта',
        'form': form,
    }
    return render(request, 'admins/admin-products-create.html', context)



@user_passes_test(lambda u: u.is_staff)
def admin_products_update(request, pk):
    selected_product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductAdminCreationForm(instance=selected_product, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminCreationForm(instance=selected_product)
    context = {
        'title': 'Админ-панель - редактирование продукта',
        'form': form,
        'selected_product': selected_product,
    }
    return render(request, 'admins/admin-products-update-delete.html', context)



@user_passes_test(lambda u: u.is_staff)
def admin_products_remove(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products'))


@user_passes_test(lambda u: u.is_staff)
def admin_categories(request):
    context = {'title': 'Админ-панель - категории', 'categories': ProductCategory.objects.all()}
    return render(request, 'admins/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_create(request):
    if request.method == 'POST':
        form = ProductAdminCategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = ProductAdminCategoryForm()

    context = {
        'title': 'Админ-панель - создание новой катгерии продуктов',
        'form': form,
    }
    return render(request, 'admins/admins-categories-create.html', context)



@user_passes_test(lambda u: u.is_staff)
def admin_categories_update(request, pk):
    selected_category = ProductCategory.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductAdminCategoryForm(instance=selected_category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = ProductAdminCategoryForm(instance=selected_category)
    context = {
        'title': 'Админ-панель - редактирование категории продукта',
        'form': form,
        'selected_category': selected_category,
    }
    return render(request, 'admins/admins-categories-update-delete.html', context)



@user_passes_test(lambda u: u.is_staff)
def admin_categories_remove(request, pk):
    product = ProductCategory.objects.get(id=pk)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admin_categories'))

# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {'title': 'Админ-панель - пользователи', 'users': User.objects.all()}
#     return render(request, 'admins/admin-users-read.html', context)

# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegistationForm()
#
#     context = {
#         'title': 'Админ-панель - создание нового пользователя',
#         'form': form,
#     }
#     return render(request, 'admins/admin-users-create.html', context)