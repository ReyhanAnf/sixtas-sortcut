# Generated by Django 4.2.7 on 2023-11-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_person_nis_alter_person_kelas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='kelamin',
        ),
        migrations.AddField(
            model_name='person',
            name='jenis_kelamin',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='jurusan',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='kelas',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
