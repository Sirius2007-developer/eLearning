# Generated by Django 4.2.6 on 2023-12-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0010_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]