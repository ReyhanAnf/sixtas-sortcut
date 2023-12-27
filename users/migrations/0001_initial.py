# Generated by Django 4.2.7 on 2023-12-27 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nis', models.CharField(blank=True, max_length=50)),
                ('kelas', models.CharField(blank=True, max_length=50)),
                ('jurusan', models.CharField(blank=True, max_length=50)),
                ('bio', models.CharField(blank=True, max_length=50)),
                ('jenis_kelamin', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nis', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
