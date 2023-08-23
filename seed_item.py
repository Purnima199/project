def create_items(num_items=10):
    for _ in range(num_items):
        title = fake.catch_phrase()
        price = random.uniform(10, 100)
        discount_price = random.uniform(5, price) if random.choice([True, False]) else None
        category = random.choice(CATEGORY_CHOICES)[0]
        label = random.choice(LABEL_CHOICES)[0]
        slug = slugify(title)
        description = fake.paragraph()
        image = fake.image_url(width=None, height=None)  # Generate a random image URL
        item = Item.objects.create(
            title=title,
            price=price,
            discount_price=discount_price,
            category=category,
            label=label,
            slug=slug,
            description=description,
            image=image
        )
        print("Created item: {}".format(item.title))
