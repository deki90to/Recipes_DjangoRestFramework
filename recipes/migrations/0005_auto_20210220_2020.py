# Generated by Django 3.1.2 on 2021-02-20 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_remove_user_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['recipe_name']},
        ),
    ]
