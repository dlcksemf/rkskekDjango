# Generated by Django 3.2.12 on 2022-03-21 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lostpetboard',
            name='user',
        ),
    ]