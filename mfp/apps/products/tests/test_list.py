from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ProductListAPITest(TestCase):

    def setUp(self):
        self.c = APIClient()

    def test_list(self):        
        response = self.c.get(
            '/products/all/'
        )
        print(dir(status))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_list2(self):
        #self.assertEqual(1, 2)
        pass
