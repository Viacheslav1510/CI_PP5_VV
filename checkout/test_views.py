from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from products.models import Album


class TestCheckoutViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_album = Album.objects.create(
            name='Test Album',
            image='img.jpg',
            price=59
        )
        self.bag = {'1': 1}
        session = self.client.session
        session['bag'] = self.bag
        session.save()
        self.test_user = User.objects.create_user(
            username='test_user',
            email='test@gmail.com',
            password='testpass123'
        )
        self.cache_checkout_data_url = reverse('cache_checkout_data')
        self.checkout_url = reverse('checkout')

    def test_checkout_view_get(self):
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
