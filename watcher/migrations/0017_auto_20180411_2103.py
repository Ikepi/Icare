# Generated by Django 2.0.3 on 2018-04-11 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0016_auto_20180411_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map',
            old_name='n_s',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='map',
            old_name='w_e',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='mapdetail',
            old_name='n_s',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='mapdetail',
            old_name='w_e',
            new_name='longitude',
        ),
    ]
