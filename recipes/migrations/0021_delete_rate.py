# Generated by Django 3.1.2 on 2021-02-25 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0020_ingredients'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rate',
        ),
    ]
