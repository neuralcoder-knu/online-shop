from django.test import SimpleTestCase
from accounts.forms import UserCreationForm, UserChangeForm, UserLoginForm, UserRegistrationForm

class UserCreationFormTests(SimpleTestCase):

    def test_user_creation_form_invalid_data(self):
        form = UserCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

class UserLoginFormTests(SimpleTestCase):
    def test_user_login_form_valid_data(self):
        form = UserLoginForm(data={'email': 'test@test.com', 'password': 'testpassword'})
        self.assertTrue(form.is_valid())

    def test_user_login_form_no_data(self):
        form = UserLoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

class UserRegistrationFormTests(SimpleTestCase):
    def test_user_registration_form_valid_data(self):
        form = UserRegistrationForm(data={
            'email': 'test@test.com',
            'full_name': 'Test User',
            'phone_number': '1234567890',
            'password': 'testpassword'
        })
        self.assertTrue(form.is_valid())

    def test_user_registration_form_no_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
