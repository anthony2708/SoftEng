# Generated by Django 3.2.9 on 2021-12-15 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsm_admin', '0005_doibong_playing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doibong',
            name='playin',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='fsm_admin.giaidau'),
        ),
    ]