from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]