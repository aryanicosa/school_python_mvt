from django.db import models

# Create your models here.

class Users(models.Model):
    role     = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username and self.password