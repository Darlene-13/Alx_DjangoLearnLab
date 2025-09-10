from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the book title")
    author = models.CharField(max_length=100, help_text="Enter the author's name")
    publication_year = models.IntegerField(help_text="Enter the publication year")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "bookshelf_book"
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"
