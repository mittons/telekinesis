from django.core.management.base import BaseCommand
from main.models import Category, Post

class Command(BaseCommand):
    help = 'Add mock data to the database'

    def handle(self, *args, **options):
        # Add categories
        categories = [
            {"name": "Fashion", "description": "All about fashion trends and styles."},
            {"name": "Food", "description": "All about food and food culture."},
            {"name": "Technology", "description": "Latest updates on technology."},
            {"name": "Travel", "description": "Explore the world with us."}
        ]
        for category in categories:
            categoryId = Category.objects.create(**category)
            categoryName = category["name"]
            # Add sample posts
            for i in range(4):
                Post.objects.create(
                    title=f'Sample {categoryName} Post {i + 1}',
                    content=f'This is a mock content for Sample {categoryName} Post {i + 1}',
                    category=categoryId
                )

        self.stdout.write(self.style.SUCCESS('Mock data added successfully!'))
