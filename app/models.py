from django.db import models

class Promo(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    views = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
