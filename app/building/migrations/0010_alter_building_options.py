# Generated by Django 4.0.1 on 2022-06-28 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0009_building_row'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['-row']},
        ),
    ]