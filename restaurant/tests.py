from django.test import TestCase
from .models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Cake', price=49.99, inventory=10)
        self.assertEqual(str(item), 'Cake : 49.99')