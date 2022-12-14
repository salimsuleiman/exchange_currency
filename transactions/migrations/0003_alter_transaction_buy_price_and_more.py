# Generated by Django 4.1.1 on 2022-09-18 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transaction_buy_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='buy_price',
            field=models.DecimalField(decimal_places=2, max_digits=70),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, max_digits=70),
        ),
    ]
