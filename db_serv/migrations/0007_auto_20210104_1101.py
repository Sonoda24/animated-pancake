# Generated by Django 3.0.8 on 2021-01-04 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_serv', '0006_auto_20210101_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='my_index',
            old_name='key_num',
            new_name='key_nums',
        ),
    ]
