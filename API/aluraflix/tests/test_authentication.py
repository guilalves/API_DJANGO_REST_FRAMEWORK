from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3bo', password='123456')

    def test_auth_user_com_credenciais_corretas(self):
        user = authenticate(username='c3bo', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_nao_autorizada(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_user_username_incorreto(self):
        user = authenticate(username='c3bb', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_auth_user_password_incorreto(self):
        user = authenticate(username='c3bo', password='1234567')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_com_user_authenticado(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
