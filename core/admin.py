from django.contrib import admin
from .models import Testimonial

# Register your models here.
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'company',
        'is_active'
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
        'company'
    )