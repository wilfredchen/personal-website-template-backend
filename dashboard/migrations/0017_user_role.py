# Generated by Django 3.2.9 on 2021-12-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_uisetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
