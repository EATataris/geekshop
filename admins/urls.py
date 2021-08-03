from django.urls import path
from admins.views import UserListView, UserCreateView, UserUpdateView, index, UserDeleteView
from admins.views import ProductsListView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView
from admins.views import CategoriesListView, CategoriesCreateView, CategoriesUpdateView, CategoriesDeleteView


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),

    path('products/', ProductsListView.as_view(), name='admin_products'),
    path('products/create/', ProductsCreateView.as_view(), name='admin_product_create'),
    path('products/update/<int:pk>/', ProductsUpdateView.as_view(), name='admin_products_update'),
    path('products/remove/<int:pk>/', ProductsDeleteView.as_view(), name='admin_products_remove'),

    path('categories/', CategoriesListView.as_view(), name='admin_categories'),
    path('categories/create/', CategoriesCreateView.as_view(), name='admin_category_create'),
    path('categories/update/<int:pk>/', CategoriesUpdateView.as_view(), name='admin_categories_update'),
    path('categories/remove/<int:pk>/', CategoriesDeleteView.as_view(), name='admin_categories_remove'),
]