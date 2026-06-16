from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    short_description = models.CharField(max_length=255)

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icon Class"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title