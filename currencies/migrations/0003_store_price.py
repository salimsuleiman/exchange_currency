# Generated by Django 4.1.1 on 2022-09-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=70),
            preserve_default=False,
        ),
    ]
