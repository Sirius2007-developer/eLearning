# Generated by Django 4.2.6 on 2023-12-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0007_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='index/img')),
                ('name', models.TextField()),
                ('rank', models.TextField()),
            ],
        ),
    ]
