from django.db import models

# Create your models here.
class Customers(models.Model):
    id=models.IntegerField(primary_key=True)
    cust_name=models.CharField(max_length=20,default="customer")
    mob=models.CharField(max_length=10,unique=True)
    amount=models.CharField(max_length=10)
    
