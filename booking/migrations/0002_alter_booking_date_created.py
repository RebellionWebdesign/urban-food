# Generated by Django 3.2.22 on 2023-11-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
