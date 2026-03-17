from django.db import models
from django.contrib.auth.models import User

class Emp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=200)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.name