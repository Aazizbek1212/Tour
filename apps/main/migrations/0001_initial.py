# Generated by Django 5.0.6 on 2024-06-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=100)),
                ('imgae', models.ImageField(blank=True, null=True, upload_to='')),
                ('travel_time', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
