from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import generics
from .models import Invoice
from .serializers import InvoiceSerializer
from . import views

# Define your views here
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

# URL patterns
urlpatterns = [
    path('', InvoiceListCreateView.as_view(), name='invoice-list'),  # List/Create invoices
    path('<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),  # Retrieve/Update/Delete invoice
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('create/', views.create_invoice, name='create_invoice'),
]
