# Generated by Django 2.0.7 on 2018-08-06 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventsession',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventsession',
            name='presenter',
        ),
        migrations.RemoveField(
            model_name='question',
            name='session',
        ),
        migrations.AddField(
            model_name='question',
            name='event',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
        migrations.DeleteModel(
            name='EventSession',
        ),
    ]