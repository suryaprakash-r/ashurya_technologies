from django.contrib import admin
from django.utils.html import format_html
from .models import Blog, Tag, Comment

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
    
    ordering = ("-created_at",)
    
    readonly_fields = ("image_preview",)
    filter_horizontal = ("tags",)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:120px;border-radius:10px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ("name", "slug")

    search_fields = ("name",)

    prepopulated_fields = {
        "slug": ("name",)
    }
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "blog",
        "is_approved",
        "created_at"
    )

    list_filter = (
        "is_approved",
        "created_at"
    )

    search_fields = (
        "name",
        "email",
        "message"
    )
    
    list_editable = ("is_approved",)

    actions = ["approve_comments", "reject_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)

    approve_comments.short_description = "Approve selected comments"

    def reject_comments(self, request, queryset):
        queryset.update(is_approved=False)

    reject_comments.short_description = "Reject selected comments"