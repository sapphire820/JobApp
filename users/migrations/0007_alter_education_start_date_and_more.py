# Generated by Django 4.1.5 on 2023-02-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_profile_bio_remove_profile_career_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
