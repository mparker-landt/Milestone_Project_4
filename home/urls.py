from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cookies/', views.cookies, name='cookies'),
    path('', views.index, name='home'),
    path('faq/', views.faq, name='faq'),
    path('privacy/', views.privacy, name='privacy'),
    path('returns/', views.returns, name='returns'),
    path('returnstart/', views.returnstart, name='returnstart'),
    path('stories/', views.stories, name='stories'),
    path('warranty/', views.warranty, name='warranty'),
]