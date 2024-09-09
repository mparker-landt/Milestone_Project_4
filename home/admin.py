from django.contrib import admin
from .models import Enquiry

# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone_number',
        'subject',
        'message',
        'signup',
        'create_date',
    )

    ordering = ('subject',)

admin.site.register(Enquiry, EnquiryAdmin)