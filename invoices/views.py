from rest_framework import viewsets
from rest_framework.response import Response
from .models import Invoice
from .serializers import InvoiceSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django.shortcuts import render
from .models import Invoice
from django.shortcuts import render, redirect
from .forms import InvoiceForm

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice_list.html', {'invoices': invoices})


class InvoicePagination(PageNumberPagination):
    page_size = 10  # Adjust page size as needed

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    pagination_class = InvoicePagination

    def list(self, request, *args, **kwargs):
        # Customizing list response for pagination
        response = super().list(request, *args, **kwargs)
        return Response(response.data)

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'create_invoice.html', {'form': form})
