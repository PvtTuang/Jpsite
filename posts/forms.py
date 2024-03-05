from django import forms
from posts.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category','quantity', 'image1', 'image2', 'image3']
