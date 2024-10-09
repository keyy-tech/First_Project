from django import forms
from invApp.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Product Name',
            'sku': 'SKU',
            'price': 'Price',
            'description': 'Description',
            'quantity': 'Quantity',
            'supplier': 'Supplier'
        }
        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description','rows': 5, 'cols': 20}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplier'}),
        }

