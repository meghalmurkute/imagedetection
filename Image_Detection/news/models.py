from django.db import models

# Create your models here.
class news(models.Model):
         title=models.CharField(max_length=50)
         news=models.TextField()
