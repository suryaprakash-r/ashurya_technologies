from django.db import models


class Contact(models.Model):

    SERVICE_CHOICES = (
        ('website', 'Website Development'),
        ('webapp', 'Web Application'),
        ('mobile', 'Mobile Application'),
        ('billing', 'Billing Software'),
        ('ai', 'AI Solution'),
        ('other', 'Other'),
    )

    STATUS_CHOICES = (

        ('new','New'),

        ('contacted','Contacted'),

        ('discussion','Discussion Scheduled'),

        ('proposal','Proposal Sent'),

        ('won','Won'),

        ('lost','Lost'),

    )

    name = models.CharField(max_length=100)

    company_name = models.CharField(
        max_length=150,
        blank=True
    )

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    remarks = models.TextField(
        blank=True
    )

    next_followup = models.DateField(
        null=True,
        blank=True
    )
    is_contacted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name