# Generated by Django 3.2.9 on 2021-11-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_user_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('short_desc', models.TextField(null=True)),
            ],
        ),
    ]
