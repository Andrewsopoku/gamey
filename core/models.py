from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class AuthUserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=100, blank=True)
    account_type= models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True,auto_now_add=True)
    country_of_citizenship = models.CharField(max_length=100, blank=True)
    country_of_residence = models.CharField(max_length=100, blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    active = models.BooleanField(default=False)

class Scheme(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=4)

class Deposits(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=4)
    quantity = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    months_paid = models.IntegerField(default=0)
    cummulated_interest = models.DecimalField(max_digits=8, decimal_places=4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class MonthlyInterest(models.Model):
    deposit = models.OneToOneField(Deposits, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=4)
    created_at = models.DateField(auto_now_add=True)



