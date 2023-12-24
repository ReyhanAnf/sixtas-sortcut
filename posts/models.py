from django.db import models
from django.utils.crypto import get_random_string
get_random_string(10).lower()

# Create your models here.
class Posts(models.Model):
    post_id = models.CharField(max_length=15, editable=False, unique=True, PrimaryKey=True)
    author_id = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post-images', blank=True)
    like = models.IntegerField(default=0)
    post_at = models.DateTimeField(False, True, editable=False)
    
    
class Answers(models.Model):
    answer_id = models.CharField(max_length=15, editable=False, unique=True, PrimaryKey=True)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, to_field='post_id')
    answerer_id = models.CharField(max_length=100)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    content = models.TextField()
    image = models.ImageField(upload_to='post-images', blank=True)
    answer_at = models.DateTimeField(False, True, editable=False)
    

class Replies(models.Model):
    reply_id = models.CharField(max_length=15, editable=False, unique=True, PrimaryKey=True)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE, to_field='answer_id')
    replier_id = models.CharField(max_length=100)
    content = models.TextField()
    reply_at = models.DateTimeField(False, True, editable=False)