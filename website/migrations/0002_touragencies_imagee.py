# Generated by Django 4.0.1 on 2023-03-28 13:00

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='touragencies',
            name='imagee',
            field=models.ImageField(default='default_value', upload_to=website.models.get_file_path),
        ),
    ]
