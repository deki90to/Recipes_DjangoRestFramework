# Generated by Django 3.1.2 on 2021-02-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0027_auto_20210228_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Ok'), (4, 'Good'), (5, 'Very Good')]),
        ),
    ]
