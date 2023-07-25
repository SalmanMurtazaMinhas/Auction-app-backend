# Generated by Django 4.2.3 on 2023-07-24 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AddField(
            model_name='user',
            name='block_number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='house_number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='money',
            field=models.CharField(default='100', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='road_number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
