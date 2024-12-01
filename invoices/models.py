from django.db import models
from decimal import Decimal

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.customer_name}"

class InvoiceDetail(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.line_total = Decimal(self.quantity) * Decimal(self.unit_price)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.quantity} x {self.unit_price}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name