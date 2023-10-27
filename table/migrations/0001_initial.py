# Generated by Django 3.2.22 on 2023-10-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('persons', models.IntegerField()),
                ('max_persons', models.IntegerField()),
                ('booked_out', models.BooleanField()),
            ],
        ),
    ]