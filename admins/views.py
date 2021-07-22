from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

from admins.forms import UserAdminRegistationForm, UserAdminProfileForm, ProductAdminCreationForm, CategoryAdminCreationForm
from users.models import User
from products.models import Product, ProductCategory
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - создание нового пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductsListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - продукты'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductsCreateView(CreateView):
    model = Product
    form_class = ProductAdminCreationForm
    template_name = 'admins/admin-products-create.html'
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - создание нового товара'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductsUpdateView(UpdateView):
    model = Product
    form_class = ProductAdminCreationForm
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - редактирование продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CategoriesListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CategoriesCreateView(CreateView):
    model = ProductCategory
    form_class = CategoryAdminCreationForm
    template_name = 'admins/admins-categories-create.html'
    success_url = reverse_lazy('admins:admin_categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - создание новой категории продуктов'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CategoriesUpdateView(UpdateView):
    model = ProductCategory
    form_class = CategoryAdminCreationForm
    template_name = 'admins/admins-categories-update-delete.html'
    success_url = reverse_lazy('admins:admin_categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - редактирование категории продуктов'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CategoriesDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admins-categories-update-delete.html'
    success_url = reverse_lazy('admins:admin_categories')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Пользователи
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

# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, pk):
#     selected_user = User.objects.get(id=pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {
#         'title': 'Админ-панель - редактирование пользователя',
#         'form': form,
#         'selected_user': selected_user,
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)

# @user_passes_test(lambda u: u.is_staff)
# def admin_users_remove(request, pk):
#     user = User.objects.get(id=pk)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users'))


# Продукты
# @user_passes_test(lambda u: u.is_staff)
# def admin_products(request):
#     context = {'title': 'Админ-панель - продукты', 'products': Product.objects.all()}
#     return render(request, 'admins/admin-products-read.html', context)

# @user_passes_test(lambda u: u.is_staff)
# def admin_product_create(request):
#     if request.method == 'POST':
#         form = ProductAdminCreationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductAdminCreationForm()
#
#     context = {
#         'title': 'Админ-панель - создание нового продукта',
#         'form': form,
#     }
#     return render(request, 'admins/admin-products-create.html', context)

# @user_passes_test(lambda u: u.is_staff)
# def admin_products_update(request, pk):
#     selected_product = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         form = ProductAdminCreationForm(instance=selected_product, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductAdminCreationForm(instance=selected_product)
#     context = {
#         'title': 'Админ-панель - редактирование продукта',
#         'form': form,
#         'selected_product': selected_product,
#     }
#     return render(request, 'admins/admin-products-update-delete.html', context)

# @user_passes_test(lambda u: u.is_staff)
# def admin_products_remove(request, pk):
#     product = Product.objects.get(id=pk)
#     product.delete()
#     return HttpResponseRedirect(reverse('admins:admin_products'))

# Категории
# @user_passes_test(lambda u: u.is_staff)
# def admin_categories(request):
#     context = {'title': 'Админ-панель - категории', 'categories': ProductCategory.objects.all()}
#     return render(request, 'admins/admin-categories-read.html', context)

# @user_passes_test(lambda u: u.is_staff)
# def admin_category_create(request):
#     if request.method == 'POST':
#         form = ProductAdminCategoryForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_categories'))
#     else:
#         form = ProductAdminCategoryForm()
#
#     context = {
#         'title': 'Админ-панель - создание новой категории продуктов',
#         'form': form,
#     }
#     return render(request, 'admins/admins-categories-create.html', context)

# @user_passes_test(lambda u: u.is_staff)
# def admin_categories_update(request, pk):
#     selected_category = ProductCategory.objects.get(id=pk)
#     if request.method == 'POST':
#         form = ProductAdminCategoryForm(instance=selected_category, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_categories'))
#     else:
#         form = ProductAdminCategoryForm(instance=selected_category)
#     context = {
#         'title': 'Админ-панель - редактирование категории продукта',
#         'form': form,
#         'selected_category': selected_category,
#     }
#     return render(request, 'admins/admins-categories-update-delete.html', context)

# @user_passes_test(lambda u: u.is_staff)
# def admin_categories_remove(request, pk):
#     category = ProductCategory.objects.get(id=pk)
#     category.delete()
#     return HttpResponseRedirect(reverse('admins:admin_categories'))