# Generated by Django 4.1.5 on 2023-02-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempsite', '0016_remove_order_user_phone_order_user_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', models.CharField(default=None, max_length=50)),
                ('user_id', models.IntegerField(default=None)),
                ('user_name', models.CharField(default=None, max_length=20)),
                ('product_id', models.JSONField(default=None)),
                ('date_time_start', models.DateTimeField(default=None)),
                ('date_time_stop', models.DateTimeField(default=None)),
            ],
        ),
    ]
