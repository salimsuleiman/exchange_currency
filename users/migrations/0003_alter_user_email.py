# Generated by Django 4.1.1 on 2022-09-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_pass_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
