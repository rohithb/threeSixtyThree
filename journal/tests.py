from django.test import TestCase
from rest_framework.test import APITestCase, APIClient

class PostTests(APITestCase):
    def create_valid_post(self):