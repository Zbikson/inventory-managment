from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    quantity_sold = models.IntegerField(null=False, blank=False)
    sales = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    stock_date = models.DateField(auto_now_add=True)
    last_sales_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name