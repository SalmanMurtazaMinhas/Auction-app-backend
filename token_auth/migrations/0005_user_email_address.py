# Generated by Django 4.2.3 on 2023-07-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_auth', '0004_user_profile_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
