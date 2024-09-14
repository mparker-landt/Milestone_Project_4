from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    """ Form for Enquiry model with fields to use and placeholders for those fields """

    class Meta:
        model = Enquiry
        fields = ('full_name', 'email', 'phone_number',
                  'subject', 'message',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'subject': 'General Enquiry',
            'message': '',
        }

        self.fields['subject'].widget.attrs['full_name'] = True
        # for field in self.fields:
        #     if field != 'country':
        #         if self.fields[field].required:
        #             placeholder = f'{placeholders[field]} *'
        #         else:
        #             placeholder = placeholders[field]
        #         self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # self.fields[field].label = False
