# Generated by Django 2.0.4 on 2018-05-10 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceList',
            fields=[
                ('number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('watchman', models.CharField(max_length=10)),
                ('fall_count', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EcgAndRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecgdata', models.TextField()),
                ('rate', models.CharField(max_length=4)),
                ('timestamp', models.TimeField()),
                ('time', models.TimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Gyr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accx', models.CharField(max_length=25)),
                ('accy', models.CharField(max_length=25)),
                ('accz', models.CharField(max_length=25)),
                ('omegax', models.CharField(max_length=25)),
                ('omegay', models.CharField(max_length=25)),
                ('omegaz', models.CharField(max_length=25)),
                ('anglex', models.CharField(max_length=25)),
                ('angley', models.CharField(max_length=25)),
                ('anglez', models.CharField(max_length=25)),
                ('fall', models.BooleanField()),
                ('timestamp', models.TimeField()),
                ('time', models.TimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('time', models.TimeField(auto_now=True)),
                ('timestamp', models.TimeField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ta', models.CharField(max_length=10)),
                ('to', models.CharField(max_length=10)),
                ('time', models.TimeField(auto_now=True)),
                ('timestamp', models.TimeField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='EcgAndRateDetail',
            fields=[
                ('ecgdata', models.TextField()),
                ('rate', models.CharField(max_length=4)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ecg_detail', serialize=False, to='watcher.DeviceList')),
                ('timestamp', models.TimeField()),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GyrDetail',
            fields=[
                ('accx', models.CharField(max_length=25)),
                ('accy', models.CharField(max_length=25)),
                ('accz', models.CharField(max_length=25)),
                ('omegax', models.CharField(max_length=25)),
                ('omegay', models.CharField(max_length=25)),
                ('omegaz', models.CharField(max_length=25)),
                ('anglex', models.CharField(max_length=25)),
                ('angley', models.CharField(max_length=25)),
                ('anglez', models.CharField(max_length=25)),
                ('fall', models.BooleanField()),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='gyr_detail', serialize=False, to='watcher.DeviceList')),
                ('timestamp', models.TimeField()),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MapDetail',
            fields=[
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('time', models.TimeField(auto_now=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='map_detail', serialize=False, to='watcher.DeviceList')),
                ('timestamp', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TempDetail',
            fields=[
                ('ta', models.CharField(max_length=10)),
                ('to', models.CharField(max_length=10)),
                ('time', models.TimeField(auto_now=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='temper_detail', serialize=False, to='watcher.DeviceList')),
                ('timestamp', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='temp',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temper', to='watcher.DeviceList'),
        ),
        migrations.AddField(
            model_name='map',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map', to='watcher.DeviceList'),
        ),
        migrations.AddField(
            model_name='gyr',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gyr', to='watcher.DeviceList'),
        ),
        migrations.AddField(
            model_name='ecgandrate',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ecg', to='watcher.DeviceList'),
        ),
        migrations.AddField(
            model_name='devicelist',
            name='user',
            field=models.ManyToManyField(related_name='devicelist', to=settings.AUTH_USER_MODEL),
        ),
    ]
