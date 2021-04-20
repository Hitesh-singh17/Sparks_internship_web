from django.db import models
import datetime
from datetime import date

# Create your models here.

class User(models.Model):

    # Creating Database for Register from
    Username = models.CharField(max_length=40)
    name  = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    balance=models.IntegerField()
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class Transfer(models.Model):

    #Transfer detail
    To=models.CharField(max_length=40)
    From= models.CharField(max_length=40)
    amount=models.IntegerField()
    date=models.DateField()


    def __str__(self):

        return self.date
