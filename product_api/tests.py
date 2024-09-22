from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product

class ProductAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': '9.99'
        }
        self.url = reverse('product-list-create')

    def test_create_valid_product(self):
        response = self.client.post(self.url, self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')

    def test_create_invalid_product(self):
        invalid_data = self.product_data.copy()
        invalid_data['price'] = -10
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_product_list(self):
        Product.objects.create(**self.product_data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_product_detail(self):
        product = Product.objects.create(**self.product_data)
        url = reverse('product-detail', kwargs={'pk': product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product_data['name'])

    def test_update_product(self):
        product = Product.objects.create(**self.product_data)
        url = reverse('product-detail', kwargs={'pk': product.id})
        updated_data = {'name': 'Updated Product', 'description': 'Updated Description', 'price': '19.99'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(id=product.id).name, 'Updated Product')

    def test_delete_product(self):
        product = Product.objects.create(**self.product_data)
        url = reverse('product-detail', kwargs={'pk': product.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

class ProductModelTests(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price='9.99'
        )
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(product.__str__(), product.name)