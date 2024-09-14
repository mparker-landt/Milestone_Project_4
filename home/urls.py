from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('cookies/', views.cookies, name='cookies'),
    path('', views.index, name='home'),
    path('enquiries/', views.enquiries, name='enquiries'),
    path('enquiry/<enquiry_number>', views.enquiry, name='enquiry'),
    path('faq/', views.faq, name='faq'),
    path('privacy/', views.privacy, name='privacy'),
]
