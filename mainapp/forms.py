from django import forms
from .models import Good

class ImageForm(forms.Form):
    image = forms.ImageField()


class GoodForm(forms.Form):
    # class Meta:
    #     model = Good
    #     fields = ['name', 'price', 'count', 'image']
    #     labels = {'name': 'Name', 'price': 'Price', 'count': 'Count', 'image': 'Image'}
    name = forms.CharField(max_length=50)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    count = forms.IntegerField()
    image = forms.ImageField(required=False)
