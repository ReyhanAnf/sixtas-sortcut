from django.db import models

# Create your models here.
class Users(models.Model):
    nis = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    
class Person(models.Model):
    nis = models.CharField(max_length=50, blank=True)
    kelas = models.CharField(max_length=50, blank=True )
    jurusan = models.CharField(max_length=50, blank=True)
    hobi = models.CharField(max_length=50, blank=True)
    jenis_kelamin = models.CharField(max_length=50, blank=True)