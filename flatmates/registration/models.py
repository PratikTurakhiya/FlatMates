from django.db import models
from datetime import datetime,date
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class t1(models.Model):
    name=models.CharField(max_length=6)
    pic=models.FileField(blank="true",null="true")

class t2(models.Model):
    name=models.CharField(max_length=7)
    pic=models.FileField(blank="true",null="true")

class t3(models.Model):
    name=models.CharField(max_length=8)
    pic=models.ImageField(blank="true",null="true",upload_to='')
    drop=models.CharField(max_length=30)
    mul=models.CharField(max_length=100)
    birthdate = models.DateTimeField(blank=True, null=True)          

class owner(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mo=PhoneNumberField()
    Pic=models.ImageField(blank="true",null="true",upload_to='')
    city=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    flattype=models.CharField(max_length=20)
    furnishing=models.CharField(max_length=20)
    avlfrom=models.DateTimeField(blank=True, null=True)
    avlupto=models.DateTimeField(blank=True, null=True)
    aminities=models.CharField(max_length=100)
    avlgen=models.CharField(max_length=20)
    des=models.CharField(max_length=200)
    price=models.IntegerField()

class roomshare(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mo=PhoneNumberField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    neighborhood=models.CharField(max_length=100)
    des=models.CharField(max_length=200)
    lgender=models.CharField(max_length=10)
    interest=models.CharField(max_length=150)
    avlfrom=models.DateTimeField(blank=True, null=True)
    avlupto=models.DateTimeField(blank=True, null=True)
    price=models.IntegerField()
    aminities=models.CharField(max_length=100)
    Pic=models.FileField(blank="true",null="true",upload_to='')
    city=models.CharField(max_length=20)
    room=models.CharField(max_length=20)
    furnishing=models.CharField(max_length=20)
    hometype=models.CharField(max_length=20)
    bath=models.CharField(max_length=20)
    parking=models.CharField(max_length=20)


class contactus(models.Model):
    name=models.CharField(max_length=20)   
    email=models.EmailField()
    subject=models.CharField(max_length=20)
    mes=models.CharField(max_length=100)

class review(models.Model):
    name=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)   
    mo=PhoneNumberField()
    email=models.EmailField()
    rating=models.CharField(max_length=10)
    des=models.CharField(max_length=100)
    
#class signup(models.Model):
 #   name =models.CharField(max_length=20)
  #  bday = models.DateField()
   # gender= models.CharField(max_length=6)
    #email =models.EmailField()
    #password=models.CharField(max_length=20)

