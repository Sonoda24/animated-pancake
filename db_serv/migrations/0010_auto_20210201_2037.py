# Generated by Django 3.0.8 on 2021-02-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_serv', '0009_auto_20210131_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(upload_to='Document/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
