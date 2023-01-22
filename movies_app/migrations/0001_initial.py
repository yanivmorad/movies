# Generated by Django 4.1.5 on 2023-01-19 13:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=256)),
                ('description', models.CharField(db_column='description', max_length=256)),
                ('duration_min', models.FloatField(db_column='duration_min')),
                ('release_year', models.IntegerField(db_column='release_year', null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(3000)])),
                ('pic_url', models.URLField(db_column='pic_url', max_length=512, null=True)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]