from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True
    )

    image = models.ImageField(
        upload_to='blogs/'
    )

    excerpt = models.TextField(
        help_text="Short summary displayed in blog cards"
    )

    content = models.TextField()

    featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    meta_description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title