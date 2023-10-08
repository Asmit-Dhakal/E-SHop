from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/recommendations/', views.product_recommendations, name='product_recommendations'),
]
