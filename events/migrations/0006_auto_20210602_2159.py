# Generated by Django 3.1.6 on 2021-06-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image_url',
            field=models.URLField(blank=True, max_length=10000),
        ),
    ]
