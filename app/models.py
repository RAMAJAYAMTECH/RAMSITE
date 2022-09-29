from django.db import models

# Create your models here.

class Messagebox(models.Model):

    Name= models.CharField(max_length=30,null=True)
    Email = models.EmailField(null=True)
    Subject = models.CharField(max_length=30,null=True)
    Message = models.CharField(max_length=30,null=True)
    