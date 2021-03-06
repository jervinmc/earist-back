# Generated by Django 4.0.5 on 2022-06-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.CharField(blank=True, max_length=255, null=True, verbose_name='floor')),
                ('label', models.CharField(blank=True, max_length=255, null=True, verbose_name='label')),
                ('image', models.CharField(blank=True, max_length=255, null=True, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
