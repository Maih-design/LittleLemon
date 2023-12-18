from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(
            title="Pasta",
            price="6.00",
            inventory="20"
        )
        Menu.objects.create(
            title="Flafel",
            price="2.00",
            inventory="30"
        )
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
    def test_getall(self):
        url = reverse("menuitems")
        response = self.client.get(url)
        items = Menu.objects.all()
        serialized_data = MenuSerializer(items, many=True).data
        
        self.assertEqual(response.data, serialized_data)