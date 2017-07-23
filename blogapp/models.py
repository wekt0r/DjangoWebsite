from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
