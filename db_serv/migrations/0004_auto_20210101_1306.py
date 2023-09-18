# Generated by Django 3.0.8 on 2021-01-01 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_serv', '0003_auto_20201101_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(blank=True, null=True, verbose_name='番号')),
                ('kind', models.CharField(blank=True, max_length=30, verbose_name='種類')),
                ('mfg', models.BooleanField(default=False, verbose_name='Modf')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='Level')),
                ('rec_num', models.IntegerField(blank=True, null=True, verbose_name='Rec_num')),
                ('key_num', models.IntegerField(blank=True, null=True, verbose_name='Key_num')),
                ('key_tags', models.TextField(blank=True, verbose_name='Keys')),
            ],
        ),
        migrations.CreateModel(
            name='My_Recs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(blank=True, null=True, verbose_name='番号')),
                ('kind', models.CharField(blank=True, max_length=30, verbose_name='種類')),
                ('mfg', models.BooleanField(default=False, verbose_name='Modf')),
                ('rec_num', models.IntegerField(blank=True, null=True, verbose_name='Rec_num')),
                ('tags', models.TextField(blank=True, verbose_name='Tags')),
            ],
        ),
        migrations.AlterModelOptions(
            name='my_svg',
            options={},
        ),
        migrations.AddField(
            model_name='my_data',
            name='author',
            field=models.CharField(blank=True, max_length=30, verbose_name='著者'),
        ),
        migrations.AddField(
            model_name='my_data',
            name='kind',
            field=models.CharField(blank=True, max_length=30, verbose_name='種類'),
        ),
        migrations.AddField(
            model_name='my_svg',
            name='kind',
            field=models.CharField(blank=True, max_length=30, verbose_name='種類'),
        ),
    ]
