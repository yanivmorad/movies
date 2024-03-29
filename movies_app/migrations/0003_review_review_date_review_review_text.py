# Generated by Django 4.1.5 on 2023-01-21 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_alter_movie_description_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_date',
            field=models.DateField(db_column='review_date', null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='review_text',
            field=models.CharField(db_column='review_text', max_length=256, null=True),
        ),
    ]
