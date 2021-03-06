# Generated by Django 3.1.2 on 2021-02-25 18:38

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0022_auto_20210225_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='email',
            new_name='user_email',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[200, 110], upload_to='pictures'),
        ),
    ]
