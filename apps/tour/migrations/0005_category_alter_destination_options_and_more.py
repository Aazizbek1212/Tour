# Generated by Django 5.0.6 on 2024-07-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_rename_name2_country_namee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='destination',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='tour',
            name='categories',
            field=models.ManyToManyField(blank=True, to='tour.category'),
        ),
    ]
