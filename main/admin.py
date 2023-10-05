from django.contrib import admin
from .models import Category, Post

# Define the admin class for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', )

# Register Category model with its admin class
admin.site.register(Category, CategoryAdmin)

# Define the admin class for Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'category')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'

# Register Post model with its admin class
admin.site.register(Post, PostAdmin)
