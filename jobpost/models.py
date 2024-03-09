from django.db import models


class reg(models.Model):
    id = models.IntegerField(primary_key = True)
    name=models.CharField(max_length=150)
    
    email=models.CharField(max_length=150)  
   
    password=models.CharField(max_length=150)  
    
    
    
class posts(models.Model):
    id = models.IntegerField(primary_key = True)
    name=models.CharField(max_length=150)
    
    description=models.CharField(max_length=150)      
    date=models.CharField(max_length=150)      
   
class upload(models.Model):
    id = models.IntegerField(primary_key = True)
    userid=models.CharField(max_length=150)
    
    job_id=models.CharField(max_length=150)      
    name=models.CharField(max_length=150)      
    email=models.CharField(max_length=150)      
    phone=models.CharField(max_length=150)      
    skill=models.CharField(max_length=150)      
    experience=models.CharField(max_length=150)      
    jsondata=models.CharField(max_length=150)      
    image=models.CharField(max_length=150)      
    personality=models.CharField(max_length=150)      
   




