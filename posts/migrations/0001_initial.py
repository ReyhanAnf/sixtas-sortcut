# Generated by Django 4.2.7 on 2023-12-27 01:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('answer_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answerer_id', models.CharField(max_length=100)),
                ('up', models.IntegerField(default=0)),
                ('down', models.IntegerField(default=0)),
                ('content_answer', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='post-images')),
                ('answer_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author_id', models.CharField(max_length=100)),
                ('content_post', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='post-images')),
                ('like', models.IntegerField(default=0)),
                ('post_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('reply_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('replier_id', models.CharField(max_length=100)),
                ('content_reply', models.TextField()),
                ('reply_at', models.DateField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.answers')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts'),
        ),
    ]
