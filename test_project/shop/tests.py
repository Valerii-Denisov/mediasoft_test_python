import json

from rest_framework.test import APITestCase
from rest_framework import status
from test_project.shop.models import Shop
from test_project.shop.serializers import ShopSerializer


# Create your tests here.
class ShopTestCase(APITestCase):
    url = 'http://127.0.0.1:8000/shop/'
    url_all = 'http://127.0.0.1:8000/shop/?street=1&city=1&open=1'
    url_without_all = 'http://127.0.0.1:8000/shop/?street=&city=&open='
    fixtures = ['shop.json', 'city.json']

    def setUp(self) -> None:
        self.shop_list = self.url
        self.shop1 = Shop.objects.get(pk=1)
        self.shop2 = Shop.objects.get(pk=2)
        self.shop3 = Shop.objects.get(pk=3)
        self.form_data = {
            "name": "test4",
            "city": 2,
            "street": 2,
            "house": 8,
            "to_open_time": "04:00:00",
            "to_close_time": "23:00:00",
        }

    def test_shop_list(self):
        response = self.client.get(self.shop_list, )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        assert_data = [
            ShopSerializer(self.shop1).data,
            ShopSerializer(self.shop2).data,
            ShopSerializer(self.shop3).data,
        ]
        self.assertEqual(response_data, assert_data)

    def test_filter_shop(self):
        response = self.client.get(self.url_all)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        assert_data = [
            ShopSerializer(self.shop1).data,
        ]
        self.assertEqual(response_data, assert_data)

    def test_shop_list_without_filter(self):
        response = self.client.get(self.url_without_all, )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        assert_data = [
            ShopSerializer(self.shop1).data,
            ShopSerializer(self.shop2).data,
            ShopSerializer(self.shop3).data,
        ]
        self.assertEqual(response_data, assert_data)

    def test_create_shop(self):
        response = self.client.post(
            self.shop_list,
            self.form_data,
            format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Shop.objects.get(pk=4))
