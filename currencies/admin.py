import imp
from django.contrib import admin

from .models import Currency, Store


admin.site.register([Currency, Store])