# Generated by Django 5.0.6 on 2024-06-29 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='name',
            new_name='title',
        ),
    ]
