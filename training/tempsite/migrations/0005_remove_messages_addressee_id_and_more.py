# Generated by Django 4.1.5 on 2023-01-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempsite', '0004_messages'),
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
        migrations.AddField(
            model_name='messages',
            name='addressee',
            field=models.CharField(default=1, max_length=20, null=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='owner',
            field=models.CharField(default=1, max_length=20, null=''),
            preserve_default=False,
        ),
    ]
