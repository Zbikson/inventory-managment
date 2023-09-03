from django.forms import ModelForm
from .models import Inventory

class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ["name", "price", "quantity", "quantity_sold"]

class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ["name", "price", "quantity", "quantity_sold"]