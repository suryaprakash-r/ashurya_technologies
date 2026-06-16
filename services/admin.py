from django.contrib import admin

from .models import Service

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active',
        'created_at',
        'updated_at'
    )

    list_filter = (
        'is_active',
        'created_at'
    )

    search_fields = (
        'title',
        'short_description'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }