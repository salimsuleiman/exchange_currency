# Generated by Django 4.1.1 on 2022-09-18 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=70)),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=70)),
                ('tx_type', models.CharField(choices=[('buy', 'buy'), ('sell', 'sell')], max_length=4)),
            ],
        ),
    ]
