# Generated by Django 4.2.6 on 2023-12-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0008_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='index/img')),
                ('name', models.TextField()),
                ('job', models.TextField()),
                ('bio', models.TextField()),
            ],
        ),
    ]