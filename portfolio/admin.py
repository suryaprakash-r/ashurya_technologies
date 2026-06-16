from django.contrib import admin
from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'featured',
        'created_at'
    )

    list_filter = (
        'featured',
        'created_at'
    )

    search_fields = (
        'title',
        'technologies'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }