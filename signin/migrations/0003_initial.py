# Generated by Django 4.0.6 on 2022-07-15 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signin', '0002_delete_nguoidung'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nhanvien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=100)),
                ('chuc_vu', models.CharField(max_length=100)),
                ('nam_sinh', models.CharField(max_length=100)),
            ],
        ),
    ]
