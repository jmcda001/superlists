from django.db import models

# Create your models here.
class Item(models.Model):
    text = models.TextField(default='')

    def __str__(self):
        return self.text
