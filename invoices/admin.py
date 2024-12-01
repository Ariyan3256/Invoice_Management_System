from django.contrib import admin
from .models import Invoice, InvoiceDetail, Customer

admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
admin.site.register(Customer)