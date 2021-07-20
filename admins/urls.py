from django.urls import path
from admins.views import admin_users, admin_users_create, admin_users_update, index, admin_users_remove
from admins.views import admin_products, admin_product_create, admin_products_update, admin_products_remove
from admins.views import admin_categories, admin_category_create, admin_categories_update, admin_categories_remove


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='admin_users_create'),
    path('users/update/<int:pk>/', admin_users_update, name='admin_users_update'),
    path('users/remove/<int:pk>/', admin_users_remove, name='admin_users_remove'),

    path('products/', admin_products, name='admin_products'),
    path('products/create/', admin_product_create, name='admin_product_create'),
    path('products/update/<int:pk>/', admin_products_update, name='admin_products_update'),
    path('products/remove/<int:pk>/', admin_products_remove, name='admin_products_remove'),

    path('categories/', admin_categories, name='admin_categories'),
    path('categories/create/', admin_category_create, name='admin_category_create'),
    path('categories/update/<int:pk>/', admin_categories_update, name='admin_categories_update'),
    path('categories/remove/<int:pk>/', admin_categories_remove, name='admin_categories_remove'),
]