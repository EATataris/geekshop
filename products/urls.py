from django.urls import path
from products.views import ProductsListView, ProductDetail
from django.views.decorators.cache import cache_page, never_cache

app_name = 'products'

urlpatterns = [
    path('', never_cache(ProductsListView.as_view()), name='index'),
    path('<int:category_id>/', never_cache(ProductsListView.as_view()), name='product'),
    path('page/<int:page>/', never_cache(ProductsListView.as_view()), name='page'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
]