from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, RentalProduct, AuctionProduct, Bid


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class RentalForm(forms.ModelForm):

    class Meta:
        model = RentalProduct
        fields = '__all__'
        widgets = {
            'rental_period': forms.TextInput(attrs={'type': 'date'})
        }

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # categories = Category.objects.all()
        # friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class AuctionForm(forms.ModelForm):

    class Meta:
        model = AuctionProduct
        fields = '__all__'
        widgets = {
            'auction_period': forms.TextInput(attrs={'type': 'date'})
        }

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # categories = Category.objects.all()
        # friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class BidForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # categories = Category.objects.all()
        # friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
