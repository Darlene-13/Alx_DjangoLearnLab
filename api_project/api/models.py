from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)

    class Meta:
        verbose_name = 'Book',
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title