from django.contrib import admin
from .models import Enquiry


class EnquiryAdmin(admin.ModelAdmin):
    """ Fields for Enquiry Model to show on admin page """

    list_display = (
        'enquiry_number',
        'full_name',
        'email',
        'phone_number',
        'subject',
        'message',
        'signup',
        'create_date'
    )

    ordering = ('create_date',)


admin.site.register(Enquiry, EnquiryAdmin)
