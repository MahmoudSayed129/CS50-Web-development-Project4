# Generated by Django 3.2.7 on 2021-09-26 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20210925_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='post',
        ),
    ]
