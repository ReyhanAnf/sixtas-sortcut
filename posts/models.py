from django.db import models
import uuid


# Create your models here.
class Posts(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author_id = models.CharField(max_length=100)
    content_post = models.TextField()
    image = models.ImageField(upload_to='post-images', blank=True)
    like = models.IntegerField(default=0)
    post_at = models.DateField(auto_now_add=True, editable=False)
    
    
class Answers(models.Model):
    answer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, to_field='post_id')
    post_id = models.CharField(max_length=100)
    answerer_id = models.CharField(max_length=100)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    content_answer = models.TextField()
    image = models.ImageField(upload_to='post-images', blank=True)
    answer_at = models.DateField(auto_now_add=True, editable=False)
    

class Replies(models.Model):
    reply_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE, to_field='answer_id')
    answer_id = models.CharField(max_length=50)
    replier_id = models.CharField(max_length=100)
    content_reply = models.TextField()
    reply_at = models.DateField(auto_now_add=True, editable=False)