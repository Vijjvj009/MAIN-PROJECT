from django.db import models
class Customer(models.Model):
    fname=models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    pin = models.CharField(max_length=30)

class Login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    status=models.IntegerField()
class Member(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    adhno = models.CharField(max_length=30)
    photo = models.FileField()
    data=models.FileField
    hname = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    pin = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    caste = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    doj = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
class Activity(models.Model):
    actname=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
class Product(models.Model):
    pname = models.CharField(max_length=30)
    srate = models.IntegerField()
    photo = models.FileField()
    data = models.FileField
    ptype = models.CharField(max_length=30)
    punit = models.CharField(max_length=30)
    dp = models.CharField(max_length=30)
    doe = models.CharField(max_length=30)
class Pstockentry(models.Model):
    pname=models.CharField(max_length=30)
    eno=models.IntegerField(default=1)
    qty=models.CharField(max_length=30)
    edate=models.CharField(max_length=30)
class Pstock(models.Model):
    pname=models.CharField(max_length=30)
    cstock=models.CharField(max_length=30)
class Actentry(models.Model):

    actname = models.IntegerField(default=1)
    actdate = models.CharField(max_length=30)
    acttime = models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
class Cart(models.Model):
    pid = models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.CharField(max_length=30)
    qty=models.IntegerField()
    gtotal=models.IntegerField()
    status = models.IntegerField()


# Create your models here.
