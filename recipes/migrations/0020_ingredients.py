# Generated by Django 3.1.2 on 2021-02-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0019_auto_20210225_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.TextField(max_length=5000)),
            ],
            options={
                'ordering': ['ingredients'],
            },
        ),
    ]