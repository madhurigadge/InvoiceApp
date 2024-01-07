from django.contrib import admin
from Home.models import  Invoice
from Home.models import  InvoiceDetail

# Register your models here.
admin.site.register( Invoice)  
admin.site.register( InvoiceDetail)  