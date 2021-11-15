from django.core.management import call_command
from django.test import TestCase
# Create your tests here.
from django.test.client import Client

from products.models import Product, ProductCategory


class TestProductsSmoke(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(name='Test')
        Product.objects.create(category=category, name='product_test', price=100)
        self.client = Client()


    def test_products_pages(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_products_product(self):
        for product_item in Product.objects.all():
            response = self.client.get(f'/products/detail/{product_item.pk}/')
            self.assertEqual(response.status_code, 200)

    def test_products_basket(self):
        response = self.client.get(f'/users/profile/')
        self.assertEqual(response.status_code, 302)


    def tearDown(self):
        pass
