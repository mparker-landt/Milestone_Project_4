from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),

    path('rental', views.rental, name='rental'),
    path('<int:rental_id>/', views.rental_detail, name='rental_detail'),
    path('add_rental/', views.add_rental, name='add_rental'),
    path('edit_rental/<int:rental_id>/', views.edit_rental, name='edit_rental'),
    path('delete_rental/<int:rental_id>/', views.delete_rental, name='delete_rental'),

    path('auction', views.auction, name='auction'),
    path('<int:auction_id>/', views.auction_detail, name='auction_detail'),
    path('add_auction/', views.add_auction, name='add_auction'),
    path('edit_auction/<int:auction_id>/', views.edit_auction, name='edit_auction'),
    path('delete_auction/<int:auction_id>/', views.delete_auction, name='delete_auction'),
]