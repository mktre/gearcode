# Generated by Django 4.2 on 2023-04-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_area_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='title',
            field=models.TextField(default='', max_length=100),
        ),
    ]