# Generated by Django 3.2.9 on 2021-12-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nationality',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
