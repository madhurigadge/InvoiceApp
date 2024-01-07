from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice

class InvoiceTests(APITestCase):
    def test_create_invoice(self):
        data = {
            'date': '2023-12-31',
            'invoice': 'INV-001',
            'customer_name': 'Test Customer',
            'details': [
                {
                    'description': 'Test Description',
                    'quantity': 2,
                    'unit_price': 10.00,
                    'price': 20.00
                }
            ]
        }
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.get().customer_name, 'Test Customer')
