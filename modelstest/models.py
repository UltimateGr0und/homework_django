from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
