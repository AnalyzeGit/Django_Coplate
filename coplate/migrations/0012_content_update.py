# Generated by Django 2.2 on 2024-11-19 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0011_change_reverse_relationships'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='cotent',
            new_name='content',
        ),
    ]
