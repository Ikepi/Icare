# Generated by Django 2.0.4 on 2018-05-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0003_auto_20180511_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecgandrate',
            name='rate',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ecgandratedetail',
            name='rate',
            field=models.CharField(max_length=10),
        ),
    ]