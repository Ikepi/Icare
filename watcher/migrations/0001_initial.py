# Generated by Django 2.0.3 on 2018-03-19 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Gyr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accx', models.DecimalField(decimal_places=10, max_digits=10)),
                ('accy', models.DecimalField(decimal_places=10, max_digits=10)),
                ('accz', models.DecimalField(decimal_places=10, max_digits=10)),
                ('omegax', models.DecimalField(decimal_places=10, max_digits=10)),
                ('omegay', models.DecimalField(decimal_places=10, max_digits=10)),
                ('omegaz', models.DecimalField(decimal_places=10, max_digits=10)),
                ('anglex', models.DecimalField(decimal_places=10, max_digits=10)),
                ('angley', models.DecimalField(decimal_places=10, max_digits=10)),
                ('anglez', models.DecimalField(decimal_places=10, max_digits=10)),
                ('fall', models.BooleanField()),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='watcher.DeviceList')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_s', models.IntegerField()),
                ('w_e', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='watcher.DeviceList')),
            ],
        ),
        migrations.CreateModel(
            name='Tem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ta', models.DecimalField(decimal_places=2, max_digits=2)),
                ('to', models.DecimalField(decimal_places=2, max_digits=2)),
                ('time', models.DateTimeField(auto_now=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temper', to='watcher.DeviceList')),
            ],
        ),
    ]