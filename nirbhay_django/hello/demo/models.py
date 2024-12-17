from django.db import models
from datetime import datetime
from django.utils import timezone
from django_countries.fields import CountryField

GENDER =[
    ('Male','Male'),
    ('Femal','Femal'),
    ('Other','Other')
]    

STATES=[
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'), 
    ('Assam','Assam'), 
    ('Bihar','Bihar'), 
    ('Chhattisgarh','Chhattisgarh'), 
    ('Goa','Goa'), 
    ('Gujarat','Gujarat'), 
    ('Haryana','Haryana'), 
    ('Himachal Pradesh','Himachal Pradesh'), 
    ('Jharkhand','Jharkhand'), 
    ('Karnataka','Karnataka'), 
    ('Kerala','Kerala'), 
    ('Madhya Pradesh','Madhya Pradesh'), 
    ('Maharashtra','Maharashtra'), 
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'), 
    ('Mizoram','Mizoram'), 
    ('Nagaland','Nagaland'), 
    ('Odisha','Odisha'), 
    ('Punjab','Punjab'), 
    ('Rajasthan','Rajasthan'), 
    ('Sikkim','Sikkim'), 
    ('Tamil Nadu','Tamil Nadu'), 
    ('Telangana','Telangana'), 
    ('Tripura','Tripura'), 
    ('Uttrakhand','Uttrakhand'), 
    ('Uttara Pradesh','Uttara Pradesh'), 
    ('West Bengal','West Bengal') 
]
        


class student(models.Model): #crate models class.
    name = models.CharField(max_length= 100)  #add models field.
    age = models.IntegerField(default= 20)
    address = models.TextField(default='')
    email = models.EmailField(default='')
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    confirmpassword =models.CharField(max_length=8) 
    date= models.DateField(default= timezone.now)
    time= models.TimeField(default= datetime.now())
    date_birth = models.DateField(default=timezone.now)    
    Photo = models.ImageField(null= True)
    country = CountryField()
    state=models.CharField(max_length=17,choices=STATES,blank=True)
    gender = models.CharField(max_length=5, choices=GENDER, blank=True)
    
    

# class student1(models.Model): 
#     name = models.CharField(max_length= 100)
#     age = models.IntegerField(default= 20)
#     adress = models.TextField(default='')
#     email =models.EmailField(default='enter your email :')
