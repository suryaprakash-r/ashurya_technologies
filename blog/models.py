from django.db import models
from ckeditor.fields import RichTextField



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    image = models.ImageField(upload_to='blogs/')
    content = RichTextField()

    excerpt = models.TextField(
        help_text="Short summary displayed in blog cards"
    )

    content = models.TextField()

    featured = models.BooleanField(default=False)

    is_published = models.BooleanField(default=True)

    meta_title = models.CharField(max_length=255, blank=True, null=True)

    meta_description = models.TextField(blank=True, null=True)

    tags = models.ManyToManyField(
        "Tag",  
        blank=True,
        related_name="blogs"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title
    
class Comment(models.Model):

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.blog.title}"