# Generated by Django 5.0.6 on 2024-07-18 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0023_review_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='tours',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tour.tour'),
        ),
    ]
