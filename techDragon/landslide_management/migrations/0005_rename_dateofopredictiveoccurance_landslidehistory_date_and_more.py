# Generated by Django 5.1.3 on 2024-12-02 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landslide_management', '0004_rename_dateofoccurance_landslidehistory_dateofopredictiveoccurance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landslidehistory',
            old_name='dateOfOPredictiveOccurance',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='landslidehistory',
            name='Occured',
        ),
    ]
