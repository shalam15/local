from django.db import models

# Create your models here.
class CodeCard(models.Model):

    title   = models.CharField(max_length=50),
    content = models.TextField(max_length=300)

    def __str__(self):
        return self.title
