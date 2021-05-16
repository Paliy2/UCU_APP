# Generated by Django 3.1.6 on 2021-04-21 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210422_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_online_meeting_link',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigAutoField(db_index=True, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
