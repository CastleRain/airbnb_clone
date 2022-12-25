from django.db import models

# Create your models here.

class House(models.Model):

    name                = models.CharField(max_length=140)
    price_per_night     = models.PositiveIntegerField() # 양수만 가능하다.
    description         = models.TextField()
    address             = models.CharField(max_length=140)
    pets_allowed        = models.BooleanField(default=True)

    def __str__(self):
        return self.name