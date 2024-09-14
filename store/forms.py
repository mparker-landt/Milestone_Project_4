from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, RentalProduct, AuctionProduct


class ProductForm(forms.ModelForm):
    """ Form for product model with fields to use and placeholders for those fields """

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
    """ Form for Rental model with fields to use and placeholders for those fields """

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
    """ Form for Auction model with fields to use and placeholders for those fields """

    class Meta:
        model = AuctionProduct
        fields = ('title', 'description', 'instrument',
                  'image_url', 'image', 'condition',
                  'base_price', 'auction_period',  )
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
    """ Form for bid in Auction model with fields to use and placeholders for those fields """

    class Meta:
        model = AuctionProduct
        fields = ('bidders', 'auction_price' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # categories = Category.objects.all()
        # friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
