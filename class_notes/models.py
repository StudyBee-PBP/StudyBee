from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
# Create your models here.
