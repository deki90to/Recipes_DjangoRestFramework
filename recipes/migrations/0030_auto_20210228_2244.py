# Generated by Django 3.1.2 on 2021-02-28 21:44

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0029_auto_20210228_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[480, 320], upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_text',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='user_email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]