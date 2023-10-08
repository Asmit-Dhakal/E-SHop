from django.shortcuts import render
from .utils import get_recommendations
from shop.models import Product  # Import the Product model


def product_recommendations(request, product_id):
    # Retrieve the current product based on the provided product_id
    current_product = Product.objects.get(pk=product_id)

    # Generate recommendations using the get_recommendations function
    recommendations = get_recommendations(current_product)

    # Render a template with the recommendations
    return render(request, 'recommendations/recommendations.html', {'recommendations': recommendations},{'current_product':current_product})
