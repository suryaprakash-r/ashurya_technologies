from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'service',
        'is_contacted',
        'created_at'
    )

    list_filter = (
        'service',
        'is_contacted',
        'created_at'
    )

    search_fields = (
        'name',
        'email',
        'phone'
    )