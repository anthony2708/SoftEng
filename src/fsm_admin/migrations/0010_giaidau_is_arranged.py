# Generated by Django 3.2.9 on 2021-12-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsm_admin', '0009_auto_20211216_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='giaidau',
            name='is_arranged',
            field=models.BooleanField(default=False),
        ),
    ]
