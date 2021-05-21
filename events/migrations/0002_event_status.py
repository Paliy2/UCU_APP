# Generated by Django 3.1.6 on 2021-05-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('r', 'To be reviewd'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1),
        ),
    ]