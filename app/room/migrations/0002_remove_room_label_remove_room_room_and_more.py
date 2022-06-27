# Generated by Django 4.0.1 on 2022-06-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='label',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room',
        ),
        migrations.AddField(
            model_name='room',
            name='building_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='building_name'),
        ),
        migrations.AddField(
            model_name='room',
            name='floor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='floor'),
        ),
        migrations.AddField(
            model_name='room',
            name='formatID',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='formatID'),
        ),
        migrations.AddField(
            model_name='room',
            name='tiles',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='tiles'),
        ),
    ]
