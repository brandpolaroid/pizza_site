# Generated by Django 4.1.5 on 2023-02-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempsite', '0021_alter_offered_date_time_start_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offered',
            name='order_price',
            field=models.IntegerField(default=0),
        ),
    ]
