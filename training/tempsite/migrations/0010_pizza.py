# Generated by Django 4.1.5 on 2023-02-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempsite', '0009_messages_owner_messages_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('picture', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
