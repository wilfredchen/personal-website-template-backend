# Generated by Django 3.2.9 on 2021-11-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_portfolios_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolios',
            name='url',
            field=models.TextField(null=True),
        ),
    ]
