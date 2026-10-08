from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

    def clean_price(self):
        price = self.cleaned_data['price']

        if price <= 0:
            raise forms.ValidationError(
                'Price must be greater than 0.'
            )

        return price

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']

        if quantity < 0:
            raise forms.ValidationError(
                'Quantity cannot be negative.'
            )

        return quantity