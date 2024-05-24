from django.test import TestCase
from shop.models import Category, Product

class CategoryModelTests(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Electronics', slug='electronics')
        self.assertEqual(category.name, 'Electronics')
        self.assertEqual(category.slug, 'electronics')

    def test_category_str(self):
        category = Category.objects.create(name='Books', slug='books')
        self.assertEqual(str(category), 'Books')

class ProductModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', slug='electronics')

    def test_product_creation(self):
        product = Product.objects.create(
            name='Laptop',
            slug='laptop',
            image='path/to/image.jpg',
            description='A powerful laptop',
            price=1000,
            status=True
        )
        product.category.add(self.category)
        self.assertEqual(product.name, 'Laptop')
        self.assertEqual(product.slug, 'laptop')
        self.assertEqual(product.price, 1000)
        self.assertTrue(product.status)
        self.assertIn(self.category, product.category.all())

    def test_product_str(self):
        product = Product.objects.create(
            name='Smartphone',
            slug='smartphone',
            image='path/to/image.jpg',
            description='A powerful smartphone',
            price=500,
            status=True
        )
        self.assertEqual(str(product), 'Smartphone')
