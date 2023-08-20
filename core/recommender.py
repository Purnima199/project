from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from sklearn.metrics.pairwise import cosine_similarity
from .models import UserInteraction

@login_required
def get_collaborative_recommendations(user, num_recommendations=5):
    # Create a user-product interaction matrix
    interactions = UserInteraction.objects.filter(user=user)
    user_product_matrix = interactions.pivot_table(index='user', columns='product', values='interaction_type', fill_value=0)

    # Calculate item-item similarity using cosine similarity
    item_similarities = cosine_similarity(user_product_matrix.T)

    # Get user's most recent interactions
    user_interactions = user_product_matrix.T[user_product_matrix.T > 0].index

    # Find similar products to user's interactions
    similar_products = item_similarities[user_interactions].sum(axis=0)
    recommended_product_indices = similar_products.argsort()[-num_recommendations:][::-1]

    recommended_products = user_product_matrix.columns[recommended_product_indices]

    return recommended_products
