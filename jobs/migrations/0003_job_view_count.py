# Generated by Django 3.1.2 on 2020-12-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20201230_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
