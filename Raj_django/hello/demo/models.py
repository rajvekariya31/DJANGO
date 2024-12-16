from django.db import models
from datetime import datetime
from django.utils import timezone
from django_countries.fields import CountryField



Gender = [
          ('m', 'male'),
          ('f', 'female'),
          ('o','others')
           
]

class stud(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField(default = 20)
    add = models.TextField(default = 'enter your address')
    email = models.EmailField(default='enter your email address')
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    cpass = models.CharField(max_length=8)
    date_and_time = models.DateTimeField(default=datetime.now())
    dob = models.DateField(default=timezone.get_current_timezone)
    flottie = models.FloatField(default=12)
    raju = models.DecimalField(max_digits=5,decimal_places=2)
    country = CountryField()
    gender = models.CharField(max_length=1 , choices=Gender , blank=True)
    photo = models.ImageField()