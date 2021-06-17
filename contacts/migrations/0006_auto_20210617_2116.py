# Generated by Django 3.2.4 on 2021-06-17 21:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20210617_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.note'),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 17, 21, 16, 23, 76028, tzinfo=utc)),
        ),
    ]
