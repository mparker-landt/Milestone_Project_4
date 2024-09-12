from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    
    class Meta:
        model = UserProfile
        exclude = ('user',)
        fields = ('user_title', 'user_firstname', 'user_surname', 'default_phone_number', 'default_email',
                'billing_street_address1', 'billing_street_address2', 'billing_town_or_city', 'billing_county', 'billing_postcode',
                'shipping_street_address1', 'shipping_street_address2', 'shipping_town_or_city', 'shipping_county', 'shipping_postcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_title': 'Title',
            'user_firstname': 'Firstname',
            'user_surname': 'Surname',
            'default_phone_number': 'Phone Number',
            'default_email': 'Email',

            'billing_street_address1': 'Street Address 1',
            'billing_street_address2': 'Street Address 2',
            'billing_town_or_city': 'Town or City',
            'billing_county': 'County, State or Locality',
            'billing_postcode': 'Postal Code',

            'shipping_street_address1': 'Street Address 1',
            'shipping_street_address2': 'Street Address 2',
            'shipping_town_or_city': 'Town or City',
            'shipping_county': 'County, State or Locality',
            'shipping_postcode': 'Postal Code',
        }

        self.fields['default_email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False