# Generated by Django 3.2.9 on 2021-12-16 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsm_admin', '0007_taikhoan'),
    ]

    operations = [
        migrations.CreateModel(
            name='TRONGTAI',
            fields=[
                ('ma_trongtai', models.BigAutoField(primary_key=True, serialize=False)),
                ('ten_trongtai', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='XEPHANG',
            fields=[
                ('ma_bxh', models.BigAutoField(primary_key=True, serialize=False)),
                ('so_tran', models.IntegerField(default=0, null=True)),
                ('banthang', models.IntegerField(default=0, null=True)),
                ('thephat', models.IntegerField(default=0, null=True)),
                ('hieuso', models.IntegerField(default=0, null=True)),
                ('so_diem', models.IntegerField(default=0, null=True)),
                ('thuhang', models.IntegerField(default=0, null=True)),
                ('bangdau', models.CharField(max_length=2)),
                ('ma_doibong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.doibong')),
                ('ma_giaidau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.giaidau')),
            ],
        ),
        migrations.CreateModel(
            name='TRANDAU',
            fields=[
                ('ma_trandau', models.BigAutoField(primary_key=True, serialize=False)),
                ('thoigian', models.DateField(null=True)),
                ('diadiem', models.CharField(max_length=50, null=True)),
                ('ma_giaidau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.giaidau')),
                ('trongtai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.trongtai')),
            ],
        ),
        migrations.CreateModel(
            name='CHITIETTRANDAU',
            fields=[
                ('ma_ct', models.BigAutoField(primary_key=True, serialize=False)),
                ('banthang_A', models.IntegerField(null=True)),
                ('banthang_B', models.IntegerField(null=True)),
                ('thephat_A', models.IntegerField(null=True)),
                ('thephat_B', models.IntegerField(null=True)),
                ('ketqua', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ketqua', to='fsm_admin.doibong')),
                ('ma_doiA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DoiA', to='fsm_admin.doibong')),
                ('ma_doiB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DoiB', to='fsm_admin.doibong')),
                ('ma_giaidau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.giaidau')),
                ('ma_trandau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.trandau')),
            ],
        ),
    ]
