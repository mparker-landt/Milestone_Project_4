from django.contrib import admin
from .models import Enquiry

# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
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