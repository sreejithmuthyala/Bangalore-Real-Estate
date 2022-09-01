from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class broker_loctions(models.Model):

    username= models.CharField(max_length=100)
    # firstname=models.CharField(max_length=100)
    # lastname=models.CharField(max_length=100)
    # email=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
class mailsbox(models.Model):

    datetime = models.TextField()
    from_user = models.CharField(max_length=100)
    subject= models.TextField()
    body = models.TextField()
    to_user = models.CharField(max_length=100)
