from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    author = models.CharField(max_length=32, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    release = models.DateField(null=True, blank=True)
    rate = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="okładki", null=True, blank=True)

    def __str__(self):
        return self.title_with_author()

    def title_with_author(self):
        return f"{self.title} ({self.author})"
