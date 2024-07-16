# Generated by Django 5.0.6 on 2024-07-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
        ('tour', '0016_remove_tour_x_tour_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_class',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='images',
            field=models.ManyToManyField(blank=True, to='main.image'),
        ),
    ]
