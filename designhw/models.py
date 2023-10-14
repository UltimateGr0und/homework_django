from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255)

