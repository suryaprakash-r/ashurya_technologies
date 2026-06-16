from django.db import models

# Create your models here.
class Contact(models.Model):

    SERVICE_CHOICES = (
        ('website', 'Website Development'),
        ('webapp', 'Web Application'),
        ('mobile', 'Mobile Application'),
        ('billing', 'Billing Software'),
        ('ai', 'AI Solution'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    message = models.TextField()

    is_contacted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name