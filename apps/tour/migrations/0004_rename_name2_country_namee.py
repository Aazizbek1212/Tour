# Generated by Django 5.0.6 on 2024-07-04 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_rename_name_country_name2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='name2',
            new_name='namee',
        ),
    ]
