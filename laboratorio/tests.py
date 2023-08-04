from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(id=1, nombre='Laboratorio 1', ciudad='Ciudad 1', pais='Pais 1')
        # Agregar más objetos de Laboratorio según sea necesario para tus pruebas

    def test_initial_data_matches_created_data(self):
        laboratorio = Laboratorio.objects.get(id=1)
        self.assertEqual(laboratorio.nombre, 'Laboratorio 1')
        self.assertEqual(laboratorio.ciudad, 'Ciudad 1')
        self.assertEqual(laboratorio.pais, 'Pais 1')

class LaboratorioConfirmDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre='Lab Test', ciudad='City Test', pais='Country Test')

    def test_confirm_delete_view_returns_200(self):
        laboratorio = Laboratorio.objects.get(id=1)
        response = self.client.get(reverse('laboratorio_confirm_delete', args=[laboratorio.id]))
        self.assertEqual(response.status_code, 200)

    def test_confirm_delete_view_uses_correct_template(self):
        laboratorio = Laboratorio.objects.get(id=1)
        response = self.client.get(reverse('laboratorio_confirm_delete', args=[laboratorio.id]))
        self.assertTemplateUsed(response, 'laboratorio_confirm_delete.html')

    def test_confirm_delete_view_content(self):
        laboratorio = Laboratorio.objects.get(id=1)
        response = self.client.get(reverse('laboratorio_confirm_delete', args=[laboratorio.id]))
        expected_content = f'¿Estás seguro de que deseas eliminar el laboratorio "{laboratorio.nombre}"?'
        self.assertContains(response, expected_content)
