from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    image = models.ImageField(
        upload_to='projects/'
    )

    short_description = models.CharField(max_length=255)

    description = models.TextField()

    technologies = models.CharField(max_length=255)

    github_url = models.URLField(blank=True)

    live_url = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title