# Generated by Django 4.0.1 on 2023-06-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
