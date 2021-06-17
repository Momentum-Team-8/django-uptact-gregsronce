# Generated by Django 3.2.4 on 2021-06-17 19:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20210617_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='note',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='note',
            name='text',
        ),
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.note'),
        ),
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 17, 19, 26, 0, 999278, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='note',
            name='note',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
