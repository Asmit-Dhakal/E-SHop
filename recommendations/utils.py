# recommendations/utils.py
from sklearn.metrics.pairwise import cosine_similarity
from shop.models import Product


def get_recommendations(current_product, num_recommendations=5):
    # Fetch all products from the database
    products = Product.objects.all()

    # Extract product prices
    product_prices = [product.price for product in products]

    # Reshape the price data to fit the input format of cosine_similarity
    product_prices = [[price] for price in product_prices]

    # Compute cosine similarity between product prices
    similarity_scores = cosine_similarity(product_prices)

    # Get the index of the current product
    current_product_index = products.index(current_product)

    # Get similarity scores for all products
    sim_scores = list(enumerate(similarity_scores[current_product_index]))

    # Sort products based on similarity scores (price similarity)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top N similar products (excluding the current product itself)
    recommended_indices = [i[0] for i in sim_scores if i[0] != current_product_index][:num_recommendations]

    # Retrieve the recommended products
    recommended_products = [products[i] for i in recommended_indices]

    return recommended_products
