from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from sklearn.metrics.pairwise import cosine_similarity
from .models import UserInteraction, Item  # Import the Item model

@login_required
def get_collaborative_recommendations(user, num_recommendations=5):
    # Get the interactions of the user
    print("Function get_collaborative_recommendations is being called.")
    user_interactions = UserInteraction.objects.filter(user=user, interaction_type=1)

    # Get the products that the user has interacted with
    user_interacted_products = [interaction.product for interaction in user_interactions]

    # Get recommendations based on products that similar users have interacted with
    similar_users = UserInteraction.objects.filter(product__in=user_interacted_products, interaction_type=1).values('user').annotate(interaction_count=Count('user')).order_by('-interaction_count')
    
    recommended_products = []
    for similar_user in similar_users:
        similar_user_products = UserInteraction.objects.filter(user=similar_user['user'], interaction_type=1).exclude(product__in=user_interacted_products).values_list('product', flat=True)
        recommended_products.extend(similar_user_products)

    recommended_products = list(set(recommended_products))[:num_recommendations]
    
    # Debug: Print recommended product titles to console
    for recommendation in recommended_products:
        print("Recommended Product Title:", recommendation.title)
    
    return recommended_products

