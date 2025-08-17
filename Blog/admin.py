from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'id')  # Show these columns
    list_filter = ('category',)                # Add sidebar filter
    search_fields = ('title', 'content')       # Add search bar




admin.site.register(Post, PostAdmin)
admin.site.register(Category)