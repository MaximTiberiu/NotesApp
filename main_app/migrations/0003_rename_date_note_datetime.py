# Generated by Django 3.2.5 on 2021-08-05 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_note_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='date',
            new_name='datetime',
        ),
    ]
