from django.test import TestCase
from aluraflix.models import Programa


class FixtureDataTestCase(TestCase):
    fixtures = ['programas_iniciais']

    def test_verifica_carregamento_da_fixture(self):
        programa_bizaro = Programa.objects.get(pk=1)
        todos_programas = Programa.objects.all()
        self.assertEqual(programa_bizaro.titulo, 'Coisas bizarras')
        self.assertEqual(len(todos_programas), 9)