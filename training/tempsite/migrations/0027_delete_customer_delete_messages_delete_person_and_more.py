# Generated by Django 4.1.5 on 2023-02-18 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempsite', '0026_remove_offered_order_status_offered_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
