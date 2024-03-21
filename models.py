from django.db import models

class Accident(models.Model):
    accident_id = models.AutoField(primary_key=True)
    acc_date = models.DateField()
    place = models.CharField(max_length=255)
    field_no = models.IntegerField()
    damage_tier = models.CharField(max_length=5)
    veh_id = models.ForeignKey('Car', on_delete=models.CASCADE)

class Car(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=20)
    year = models.IntegerField()
    plate_no = models.CharField(max_length=45, unique=True)
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    dob = models.DateField()
    mobile_no = models.BigIntegerField()
    email = models.EmailField()

class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    mode = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()
    p_no = models.ForeignKey('Policy', on_delete=models.SET_NULL, null=True)

class Policy(models.Model):
    poly_no = models.AutoField(primary_key=True)
    date_issued = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
