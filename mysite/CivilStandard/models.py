from django.db import models

# Create your models here.
class Standard(models.Model):
    title = models.CharField(max_length=100)
    codeID = models.CharField(max_length=100)
    published_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title