# Generated by Django 3.2.4 on 2021-06-18 01:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0017_alter_note_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='note',
        ),
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 18, 1, 47, 39, 376654, tzinfo=utc)),
        ),
    ]
