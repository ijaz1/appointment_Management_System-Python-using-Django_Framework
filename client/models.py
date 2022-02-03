from django.db import models

import client

# Create your models here.

class Client(models.Model):
    first_Name=models.CharField(max_length=50)
    last_Name=models.CharField(max_length=50)
    phone_Number=models.BigIntegerField()
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=10)

class WebTimeSlot(models.Model):
    scheduled_Date=models.DateField()
    scheduled_Time=models.CharField(max_length=20)
    status=models.CharField(max_length=20)

class AppTimeSlot(models.Model):
    scheduled_Date=models.DateField()
    scheduled_Time=models.CharField(max_length=20)
    status=models.CharField(max_length=20)

class BookedWebTimeSlots(models.Model):
    client_id=models.CharField(max_length=10)
    slot_id=models.CharField(max_length=10)
    scheduled_Date=models.DateField(null=True)
    scheduled_Time=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)
    client_Name=models.CharField(max_length=50,null=True)
    client_email=models.CharField(max_length=50,null=True)
    client_phone=models.CharField(max_length=50,null=True)

class BookedAppTimeSlots(models.Model):
    client_id=models.CharField(max_length=10)
    slot_id=models.CharField(max_length=10)
    scheduled_Date=models.DateField(null=True)
    scheduled_Time=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)
    client_Name=models.CharField(max_length=50,null=True)
    client_email=models.CharField(max_length=50,null=True)
    client_phone=models.CharField(max_length=50,null=True)
    
    
