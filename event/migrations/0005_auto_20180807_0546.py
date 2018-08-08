# Generated by Django 2.0.7 on 2018-08-07 05:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20180807_0545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_id',
        ),
        migrations.AddField(
            model_name='event',
            name='id',
            field=models.CharField(default=uuid.UUID('cbb38728-0e64-4d2c-a4a1-96babd588b41'), max_length=64, primary_key=True, serialize=False, verbose_name='Event Id'),
        ),
    ]