from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=100)

    designation = models.CharField(max_length=100)

    company = models.CharField(max_length=100)

    review = models.TextField()

    image = models.ImageField(
        upload_to='testimonials/',
        blank=True
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name