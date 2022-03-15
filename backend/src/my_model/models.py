from django.db import models

# Create your models here.

class MyProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    product_code = models.TextField()
    visibility = models.BooleanField(blank=True)
    currency_type = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    requester_ip = models.GenericIPAddressField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)