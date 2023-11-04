from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    author = models.CharField(max_length=50, null=False, blank=False)
    created_date = models.DateTimeField(null=False, blank=False)
    published_date = models.DateTimeField(null=False, blank=False)


    def __str__(self):
        return f"{self.title} by {self.author}"

    