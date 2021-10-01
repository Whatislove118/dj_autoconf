# Generated by Django 3.2.7 on 2021-09-23 15:34

import configurations.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='path_to_file',
            field=models.FileField(default='default_config.py', upload_to=configurations.models.generate_config_upload_url),
        ),
    ]
