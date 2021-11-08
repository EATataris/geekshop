from django.urls import path
from products.views import ProductsListView, ProductDetail
from django.views.decorators.cache import cache_page

app_name = 'products'

urlpatterns = [
    path('', cache_page(3600)(ProductsListView.as_view()), name='index'),
    path('<int:category_id>/', cache_page(3600)(ProductsListView.as_view()), name='product'),
    path('page/<int:page>/', cache_page(3600)(ProductsListView.as_view()), name='page'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
]