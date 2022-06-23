from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import User


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        email = "test@gmail.com"
        password = "1234"
        user = User.objects.create_user(
            email=email,
            password=password,
        )
        # user = get_user_model().objects.create_user(
        #     email=self.normalize(email),
        #     password=password,
        # )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    # def test_email_is_normalised(self):

    #     sample_emails = [['test1@ExAMPLE.com', 'test1@example.com'],
    #                     ['TEST2@Example.com', 'Test2@example.com'],
    #                     ['TEST3@EXAMPLE.COM', 'Test3@example.com'],
    #                     ['test4@example.COM', 'test4@example.com']]

    #     for email, expected in sample_emails:
    #         user = User.objects.create_user(email, 'sample123')
    #         self.assertEqual(user.email, expected)

    def test_user_without_email_raise_error(self):

        with self.assertRaises(ValueError):
            User.objects.create_user("", "test123")

    def test_create_super_user(self):
        user = User.objects.create_superuser("test@example.com", "test123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
