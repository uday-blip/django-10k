from django.db import models


# Create your models here.
class Students(models.Model):
    id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=50)
    roll_no=models.IntegerField(default=1)
    
