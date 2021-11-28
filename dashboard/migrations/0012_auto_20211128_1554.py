# Generated by Django 3.2.9 on 2021-11-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_portfolios_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='portfolios',
        ),
        migrations.AddField(
            model_name='portfolios',
            name='tags',
            field=models.ManyToManyField(blank=True, to='dashboard.Tags'),
        ),
    ]
