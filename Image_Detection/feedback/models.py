from django.db import models

# Create your models here.
class feedback(models.Model):
         name=models.CharField(max_length=50)
         email_id=models.EmailField()
         issue=models.TextField()
