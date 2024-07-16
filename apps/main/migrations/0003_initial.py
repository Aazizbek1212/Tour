# Generated by Django 5.0.6 on 2024-07-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
