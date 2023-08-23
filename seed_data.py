import random
from django.contrib.auth.models import User
from core.models import Item, UserInteraction

# Define the number of interactions per user and the desired total interactions
num_interactions_per_user = 10
desired_total_interactions = 500  # Adjust this as needed

# Get all existing users and items
users = list(User.objects.all())  # Convert QuerySet to list
items = Item.objects.all()

# Generate interactions
total_interactions = 0
while total_interactions < desired_total_interactions:
    random.shuffle(users)  # Randomize user order
    for user in users:
        for _ in range(num_interactions_per_user):
            interaction = random.choice(items)
            interaction_type = random.choice([0, 1])
            UserInteraction.objects.create(user=user, product=interaction, interaction_type=interaction_type)
            total_interactions += 1
            print("Added interaction {}/{}".format(total_interactions, desired_total_interactions))

print("Generated {} interactions per user for {} users.".format(num_interactions_per_user, len(users)))
