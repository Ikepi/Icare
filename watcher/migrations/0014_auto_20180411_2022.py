# Generated by Django 2.0.3 on 2018-04-11 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0013_auto_20180404_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='gyr',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='gyr',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='gyrdetail',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='gyrdetail',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='map',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='mapdetail',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='temp',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tempdetail',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]