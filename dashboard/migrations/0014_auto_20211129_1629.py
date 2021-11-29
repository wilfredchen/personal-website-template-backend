# Generated by Django 3.2.9 on 2021-11-29 16:29

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_portfolios_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cv_path',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='images'),
        ),
    ]
