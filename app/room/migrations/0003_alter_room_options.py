# Generated by Django 4.0.1 on 2022-06-21 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_remove_room_label_remove_room_room_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['id']},
        ),
    ]
