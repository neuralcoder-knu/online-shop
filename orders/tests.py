from django.test import TestCase
from django.contrib.auth import get_user_model
from orders.models import Order, OrderItem, Coupon
from shop.models import Product
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class OrderModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test Product', price=100)
        self.order = Order.objects.create(user=self.user)
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, price=100, quantity=2)
        self.coupon = Coupon.objects.create(
            code='TESTCOUPON',
            valid_from=timezone.now() - timedelta(days=1),
            valid_to=timezone.now() + timedelta(days=1),
            discount=10,
            status=True
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user.username, 'testuser')
        self.assertFalse(self.order.status)
        self.assertEqual(self.order.get_total_price, 200)

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.get_cost(), 200)

    def test_coupon_creation(self):
        self.assertEqual(self.coupon.code, 'TESTCOUPON')
        self.assertTrue(self.coupon.status)
        self.assertTrue(self.coupon.valid_from < timezone.now())
        self.assertTrue(self.coupon.valid_to > timezone.now())

    def test_order_with_coupon(self):
        self.order.discount = self.coupon.discount
        self.order.save()
        self.assertEqual(self.order.get_total_price, 180)

