# Generated by Django 4.2.13 on 2024-06-03 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_title_about_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='author',
        ),
    ]
