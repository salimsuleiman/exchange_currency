from operator import mod
from django.db import models



# Create your models here.


class Currency(models.Model):
    sell_price = models.DecimalField(max_digits=70, decimal_places=2)
    buy_price = models.DecimalField(max_digits=70, decimal_places=2)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=12)

    def __str__(self) -> str:
        return f'{self.name} {self.symbol}'