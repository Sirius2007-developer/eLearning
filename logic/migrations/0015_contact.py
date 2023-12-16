# Generated by Django 4.2.6 on 2023-12-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0014_remove_newsletter_bio_remove_newsletter_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]