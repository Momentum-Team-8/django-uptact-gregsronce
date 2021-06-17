# Generated by Django 3.2.4 on 2021-06-17 21:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20210617_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.note'),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 17, 21, 17, 53, 345198, tzinfo=utc)),
        ),
    ]
