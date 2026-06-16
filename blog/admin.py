from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'featured',
        'is_published',
        'created_at'
    )

    list_filter = (
        'featured',
        'is_published',
        'created_at'
    )

    search_fields = (
        'title',
        'excerpt',
        'content'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }