# Generated by Django 3.1.6 on 2021-05-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210422_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
