from django.core.management.base import BaseCommand
from main.models import Category, Post

class Command(BaseCommand):
    help = 'Clear data from the Category and Post models'

    def handle(self, *args, **kwargs):
        # First, we'll delete Posts since they have a ForeignKey to Category.
        # Deleting a Category with existing Posts would result in an IntegrityError.
        Post.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all Posts'))

        # Now, delete Categories
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all Categories'))
