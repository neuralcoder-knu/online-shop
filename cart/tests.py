from django.test import TestCase
from cart.forms import Add2CartForm


class Add2CartFormTests(TestCase):

    def test_valid_form(self):
        form_data = {'quantity': 5}
        form = Add2CartForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_too_high(self):
        form_data = {'quantity': 10}
        form = Add2CartForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_too_low(self):
        form_data = {'quantity': 0}
        form = Add2CartForm(data=form_data)
        self.assertFalse(form.is_valid())
