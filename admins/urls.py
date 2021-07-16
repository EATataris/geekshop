from django.urls import path
from admins.views import admin_users, admin_users_create, admin_users_update_delete, index

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
]