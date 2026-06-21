from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    image = models.ImageField(
        upload_to='projects/'
    )

    short_description = models.CharField(max_length=255)

    description = CKEditor5Field(
        'Project Description',
        config_name='extends'
    )

    technologies = models.CharField(max_length=255)

    github_url = models.URLField(blank=True)

    live_url = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


    project_type = models.CharField(
        max_length=100,
        blank=True
    )

    completion_date = models.DateField(
        null=True,
        blank=True
    )
    
    STATUS_CHOICES = (
        ('planning', 'Planning'),
        ('development', 'Development'),
        ('testing', 'Testing'),
        ('deployment', 'Deployment'),
        ('completed', 'Completed'),
    )

    client_name = models.CharField(
        max_length=150,
        blank=True
    )

    client_email = models.EmailField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='planning'
    )

    progress = models.IntegerField(
        default=0
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    delivery_date = models.DateField(
        null=True,
        blank=True
    )

    internal_notes = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.title