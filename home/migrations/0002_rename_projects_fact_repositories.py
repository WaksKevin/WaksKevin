# Generated by Django 4.2.5 on 2023-10-07 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fact',
            old_name='projects',
            new_name='repositories',
        ),
    ]
