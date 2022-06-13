from django import forms
from product.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        # fields=['product','customer']
