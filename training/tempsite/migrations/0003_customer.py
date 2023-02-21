# Generated by Django 4.1.5 on 2023-01-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempsite', '0002_rename_user_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('password', models.CharField(default='None', max_length=20)),
                ('email', models.CharField(default='None', max_length=50)),
            ],
        ),
    ]
