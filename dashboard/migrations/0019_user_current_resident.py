# Generated by Django 3.2.9 on 2021-12-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20211209_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='current_resident',
            field=models.CharField(max_length=250, null=True),
        ),
    ]