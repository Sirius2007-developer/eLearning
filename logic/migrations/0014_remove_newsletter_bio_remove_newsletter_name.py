# Generated by Django 4.2.6 on 2023-12-14 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0013_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='name',
        ),
    ]
