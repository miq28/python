from django.db import models

# Create your models here.

class Profile(models.Model):
    nama_lengkap = models.CharField(max_length=225)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar/')
    