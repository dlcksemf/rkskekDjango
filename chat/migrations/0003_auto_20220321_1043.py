# Generated by Django 3.2.12 on 2022-03-21 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_lostpetboard_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lostpetboard',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='lostpetboard',
            name='lost_location',
        ),
        migrations.RemoveField(
            model_name='lostpetboard',
            name='pet_name',
        ),
        migrations.RemoveField(
            model_name='lostpetboard',
            name='size',
        ),
    ]
