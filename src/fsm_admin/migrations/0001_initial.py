# Generated by Django 3.2.9 on 2021-12-18 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DOIBONG',
            fields=[
                ('ma_doibong', models.BigAutoField(primary_key=True, serialize=False)),
                ('ten_doibong', models.CharField(max_length=50)),
                ('mauao_chinh', models.CharField(max_length=10)),
                ('mauao_phu', models.CharField(max_length=10)),
                ('playing', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GIAIDAU',
            fields=[
                ('ma_giaidau', models.BigAutoField(primary_key=True, serialize=False)),
                ('ten_giaidau', models.CharField(max_length=50)),
                ('sodoi_thamdu', models.IntegerField()),
                ('thethuc', models.CharField(max_length=50)),
                ('luatuoi', models.IntegerField()),
                ('lephi', models.IntegerField()),
                ('loaisan', models.IntegerField()),
                ('chedo', models.IntegerField()),
                ('trangthai', models.CharField(max_length=50)),
                ('sodoi_hientai', models.IntegerField(default=0)),
                ('is_arranged', models.BooleanField(default=False)),
            ],
        ),
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
                ('so_tran', models.IntegerField(default=0)),
                ('banthang', models.IntegerField(default=0)),
                ('thephat', models.IntegerField(default=0)),
                ('hieuso', models.IntegerField(default=0)),
                ('so_diem', models.IntegerField(default=0)),
                ('thuhang', models.IntegerField(default=0)),
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
            name='TAIKHOAN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoten', models.CharField(max_length=20)),
                ('ngaysinh', models.DateField()),
                ('gioitinh', models.CharField(max_length=5)),
                ('diachi', models.CharField(max_length=50)),
                ('so_dienthoai', models.CharField(max_length=15)),
                ('ma_taikhoan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HLVIEN',
            fields=[
                ('ma_hlv', models.BigAutoField(primary_key=True, serialize=False)),
                ('ten_hlv', models.CharField(max_length=50)),
                ('vaitro', models.CharField(max_length=20)),
                ('ma_doibong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.doibong')),
            ],
        ),
        migrations.CreateModel(
            name='HAUCAN',
            fields=[
                ('ma_haucan', models.BigAutoField(primary_key=True, serialize=False)),
                ('ten_haucan', models.CharField(max_length=50)),
                ('ma_doibong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.doibong')),
            ],
        ),
        migrations.AddField(
            model_name='doibong',
            name='playin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fsm_admin.giaidau'),
        ),
        migrations.AddField(
            model_name='doibong',
            name='ten_taikhoan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CHITIETTRANDAU',
            fields=[
                ('ma_ct', models.BigAutoField(primary_key=True, serialize=False)),
                ('banthang_A', models.IntegerField(null=True)),
                ('banthang_B', models.IntegerField(null=True)),
                ('thephat_A', models.IntegerField(null=True)),
                ('thephat_B', models.IntegerField(null=True)),
                ('tinhchat', models.CharField(default='', max_length=10, null=True)),
                ('ketqua', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ketqua', to='fsm_admin.doibong')),
                ('ma_doiA', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DoiA', to='fsm_admin.doibong')),
                ('ma_doiB', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DoiB', to='fsm_admin.doibong')),
                ('ma_giaidau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.giaidau')),
                ('ma_trandau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.trandau')),
            ],
        ),
        migrations.CreateModel(
            name='CAUTHU',
            fields=[
                ('ma_cauthu', models.BigAutoField(primary_key=True, serialize=False)),
                ('ten_cauthu', models.CharField(max_length=50)),
                ('dotuoi', models.IntegerField()),
                ('so_ao', models.IntegerField()),
                ('vitri_thidau', models.CharField(max_length=20)),
                ('ma_doibong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsm_admin.doibong')),
            ],
        ),
    ]
