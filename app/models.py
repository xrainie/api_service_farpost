from django.db import models

class Promo(models.Model):
    title = models.CharField(max_length=255)
    promo_id = models.IntegerField()
    author = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
