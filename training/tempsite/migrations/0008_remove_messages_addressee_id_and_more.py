# Generated by Django 4.1.5 on 2023-01-07 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tempsite', '0007_remove_messages_owner_remove_messages_to_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='addressee_id',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='owner_id',
        ),
    ]
