# Generated by Django 3.2.9 on 2021-12-14 11:09

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_path',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='images'),
        ),
    ]
