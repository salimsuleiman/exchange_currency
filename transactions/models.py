from distutils.sysconfig import customize_compiler
from enum import auto
from locale import currency
from operator import mod
from django.db import models
from currencies.models import Currency


class Transaction(models.Model):
     date = models.DateTimeField(auto_now=True)
     sell_price = models.DecimalField(max_digits=70, decimal_places=2)
     buy_price = models.DecimalField(max_digits=70, decimal_places=2)
     tx_type = models.CharField(max_length=4, choices=[
        ("buy", "buy"),
         ("sell", "sell")
     ])
     price = models.DecimalField(max_digits=70, decimal_places=2)
     currency = models.ForeignKey(Currency, on_delete=models.SET_DEFAULT, default=None, null=True, related_name="crn")
     currency_to = models.ForeignKey(Currency, on_delete=models.SET_DEFAULT, default=None, null=True, related_name="crn2")



    
     def __str__(self) -> str:
          return f'from {self.currency} -> {self.currency_to}'

