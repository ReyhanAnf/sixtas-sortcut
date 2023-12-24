from django.db import models
from django.utils.crypto import get_random_string
get_random_string(10).lower()

# Create your models here.
class Posts(models.Model):
    id = models.CharField(max_length=15, editable=False, unique=True, PrimaryKey=True)
    author_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(False, True, editable=False)
    content = models.TextField()
    image = models.ImageField(upload_to='post-images', blank=True)
    like = models.IntegerField(default=0)
    
    
class Answers(models.Model):
    id = models.CharField(max_length=15, editable=False, unique=True, PrimaryKey=True)
    post_id = models.ForeignKey()
    answerer_id = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=50, blank=True)
    jenis_kelamin = models.CharField(max_length=50, blank=True)
    

class Reply(models.Model):
    nis = models.CharField(max_length=50, blank=True)
    kelas = models.CharField(max_length=50, blank=True )
    jurusan = models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=50, blank=True)
    jenis_kelamin = models.CharField(max_length=50, blank=True)