# Generated by Django 4.2 on 2023-04-29 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_profile_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='group',
        ),
    ]
