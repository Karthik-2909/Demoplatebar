from django.db import models

# Create your models here.
class HCA_details(models.Model):
    name=models.CharField(max_length=10,default=None)
    FAD=models.FloatField()
    T_H_In=models.FloatField()
    P_input=models.FloatField()
    Q_input=models.FloatField()

class users(models.Model):
    name=models.CharField(max_length=100,default=None)
    userID=models.CharField(max_length=100,default=None)
    Email=models.EmailField(max_length=100,default=None)
    Phone=models.CharField(max_length=100,default=None)
    DOB=models.DateField()
    password=models.CharField(max_length=200,default=None)

    
