# Generated by Django 4.0.2 on 2022-03-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique_for_date='published'),
        ),
    ]